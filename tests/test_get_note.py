"""
GetNote Extractor 测试脚本
测试核心功能模块
"""

import unittest
import sys
import os

# 添加 src 目录到路径
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from get_note import (
    extract_topic_id,
    extract_follow_name,
    sanitize_filename,
    get_unique_output_dir
)


class TestExtractTopicId(unittest.TestCase):
    """测试知识库 ID 提取功能"""

    def test_extract_from_full_url(self):
        """从完整 URL 提取 ID"""
        url = "https://www.biji.com/subject/QYARpjM0/DEFAULT?followId=785142"
        self.assertEqual(extract_topic_id(url), "QYARpjM0")

    def test_extract_from_simple_id(self):
        """直接使用 ID"""
        self.assertEqual(extract_topic_id("ABC123"), "ABC123")

    def test_extract_complex_url(self):
        """复杂 URL 提取"""
        url = "https://www.biji.com/subject/XYZ789/DEFAULT?page=2&followName=test"
        self.assertEqual(extract_topic_id(url), "XYZ789")


class TestExtractFollowName(unittest.TestCase):
    """测试博主名称提取功能"""

    def test_extract_name_from_url(self):
        """从 URL 提取博主名称"""
        url = "https://www.biji.com/subject/QYARpjM0/DEFAULT?followId=785142&followName=张三"
        self.assertEqual(extract_follow_name(url), "张三")

    def test_extract_encoded_name(self):
        """提取 URL 编码的名称"""
        url = "https://www.biji.com/subject/ABC123/DEFAULT?followName=%E6%9D%8E%E5%9B%9B"
        result = extract_follow_name(url)
        self.assertIsNotNone(result)

    def test_no_name_in_url(self):
        """URL 中没有博主名称"""
        url = "https://www.biji.com/subject/ABC123/DEFAULT"
        self.assertIsNone(extract_follow_name(url))

    def test_invalid_url(self):
        """无效 URL"""
        self.assertIsNone(extract_follow_name("not-a-url"))


class TestSanitizeFilename(unittest.TestCase):
    """测试文件名清理功能"""

    def test_remove_invalid_chars(self):
        """移除非法字符"""
        self.assertEqual(sanitize_filename("test<>file"), "testfile")
        self.assertEqual(sanitize_filename('test:file'), "testfile")
        self.assertEqual(sanitize_filename('test"file'), "testfile")

    def test_remove_path_chars(self):
        """移除路径字符"""
        self.assertEqual(sanitize_filename("test/file\\name"), "testfilename")

    def test_limit_length(self):
        """限制文件名长度"""
        long_name = "a" * 150
        result = sanitize_filename(long_name)
        self.assertEqual(len(result), 100)

    def test_preserve_valid_chars(self):
        """保留合法字符"""
        self.assertEqual(sanitize_filename("测试文件-123.txt"), "测试文件-123.txt")
        self.assertEqual(sanitize_filename("file_name.txt"), "file_name.txt")

    def test_whitespace_handling(self):
        """处理空白字符"""
        self.assertEqual(sanitize_filename("  test  "), "test")


class TestGetUniqueOutputDir(unittest.TestCase):
    """测试输出目录命名功能"""

    def setUp(self):
        """设置测试环境"""
        self.test_dirs = []

    def tearDown(self):
        """清理测试目录"""
        for dir_path in self.test_dirs:
            if os.path.exists(dir_path):
                try:
                    os.rmdir(dir_path)
                except:
                    pass

    def test_new_directory(self):
        """创建新目录"""
        result = get_unique_output_dir("test_new_dir")
        self.test_dirs.append(result)
        self.assertTrue(result.endswith("test_new_dir"))

    def test_duplicate_directory(self):
        """处理重复目录名"""
        # 创建第一个目录
        first_dir = "./test_duplicate"
        os.makedirs(first_dir, exist_ok=True)
        self.test_dirs.append(first_dir)

        # 应该返回带数字后缀的目录名
        second_dir = get_unique_output_dir("test_duplicate")
        self.test_dirs.append(second_dir)
        self.assertTrue(second_dir.endswith("test_duplicate_2"))


class TestIntegration(unittest.TestCase):
    """集成测试"""

    def test_complete_url_parsing_workflow(self):
        """测试完整的 URL 解析流程"""
        url = "https://www.biji.com/subject/TEST123/DEFAULT?followId=123&followName=测试博主"

        # 提取 ID
        topic_id = extract_topic_id(url)
        self.assertEqual(topic_id, "TEST123")

        # 提取名称
        follow_name = extract_follow_name(url)
        self.assertEqual(follow_name, "测试博主")

        # 生成文件名
        safe_name = sanitize_filename(follow_name)
        self.assertEqual(safe_name, "测试博主")

    def test_article_title_to_filename(self):
        """测试文章标题转换为文件名"""
        titles = [
            ("正常标题", "正常标题"),
            ("标题<包含>特殊:字符", "标题包含特殊字符"),
        ]

        for title, expected in titles:
            result = sanitize_filename(title)
            self.assertEqual(result, expected)

        # 单独测试长标题截断
        long_title = "非常" * 50  # 超过100字符
        result = sanitize_filename(long_title)
        self.assertEqual(len(result), 100)


def run_tests():
    """运行所有测试"""
    print("=" * 60)
    print("  GetNote Extractor 测试套件")
    print("=" * 60)
    print()

    # 创建测试套件
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    # 添加所有测试类
    suite.addTests(loader.loadTestsFromTestCase(TestExtractTopicId))
    suite.addTests(loader.loadTestsFromTestCase(TestExtractFollowName))
    suite.addTests(loader.loadTestsFromTestCase(TestSanitizeFilename))
    suite.addTests(loader.loadTestsFromTestCase(TestGetUniqueOutputDir))
    suite.addTests(loader.loadTestsFromTestCase(TestIntegration))

    # 运行测试
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

    # 打印摘要
    print()
    print("=" * 60)
    print("  测试摘要")
    print("=" * 60)
    print(f"运行测试: {result.testsRun}")
    print(f"成功: {result.testsRun - len(result.failures) - len(result.errors)}")
    print(f"失败: {len(result.failures)}")
    print(f"错误: {len(result.errors)}")
    print("=" * 60)

    return result.wasSuccessful()


if __name__ == "__main__":
    success = run_tests()
    sys.exit(0 if success else 1)
