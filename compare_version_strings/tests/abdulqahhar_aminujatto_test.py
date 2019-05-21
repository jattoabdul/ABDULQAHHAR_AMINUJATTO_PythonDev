import pytest
from ..compare_version_strings import compare_versions, prepare_comparison_result


class TestClass:
    class TestCompareVersion:
        def test_versions_same_length_first_bigger_case1(self):
            assert compare_versions('1.2.1', '1.2.0') > 0,\
                "Should return a +ve number if first version is bigger than the second with same length [case 1]"

        def test_versions_same_length_first_bigger_case2(self):
            assert compare_versions('1.4.  1.0', ' 1.4.0.6') > 0,\
                "Should return a +ve number if first version is bigger than the second with same length [case 2]"

        def test_versions_same_length_first_bigger_case3(self):
            assert compare_versions(' 5', '1  ') > 0,\
                "Should return a +ve number if first version is bigger than the second with same length [case 3]"

        def test_versions_same_length_second_bigger_case1(self):
            assert compare_versions(' 1 .2.0  ', ' 1.2 .1') < 0,\
                "Should return a +ve number if first version is smaller than the second with same length [case 1]"

        def test_versions_same_length_second_bigger_case2(self):
            assert compare_versions('1.4.0.6  ', '  1.4.1.0') < 0,\
                "Should return a -ve number if first version is smaller than the second with same length [case 2]"

        def test_versions_same_length_second_bigger_case3(self):
            assert compare_versions('1', '  5') < 0,\
                "Should return a -ve number if first version is smaller than the second with same length [case 3]"

        def test_versions_same_length_equals(self):
            assert compare_versions(' 1.2.3  ', '1.2.3') == 0,\
                "Should return zero if are equal with same length"

        def test_versions_different_length_first_bigger_case1(self):
            assert compare_versions('1.2.1.0.0.0.1', '1.2.0.2.9.0.1.2.1.2.3.5') > 0,\
                "Should return a +ve number if first version is bigger than the second with different length [case 1]"

        def test_versions_different_length_first_bigger_case2(self):
            assert compare_versions('1.4.  1.0.0.0.0.0.0', ' 1.4.0.6') > 0,\
                "Should return a +ve number if first version is bigger than the second with different length [case 2]"

        def test_versions_different_length_first_bigger_case3(self):
            assert compare_versions(' 5', '1  .0.0.0. 0') > 0,\
                "Should return a +ve number if first version is bigger than the second with different length [case 3]"

        def test_versions_different_length_second_bigger_case1(self):
            assert compare_versions(' 1 .2.0.2.2.3.5.7.1  ', ' 1.2 .1.0.0.1') < 0,\
                "Should return a -ve number if first version is smaller than the second with different length [case 1]"

        def test_versions_different_length_second_bigger_case2(self):
            assert compare_versions('1.4.0.6.0.0  ', '  1.4.1.0.0.9.0.5') < 0,\
                "Should return a -ve number if first version is smaller than the second with different length [case 2]"

        def test_versions_different_length_second_bigger_case3(self):
            assert compare_versions('1.0', '  5.9.8.5.2') < 0,\
                "Should return a -ve number if first version is smaller than the second with different length [case 3]"

        def test_versions_different_length_equals_case1(self):
            assert compare_versions(' 1.2.3  .0.0.0.0.0.0', '1.2.3') == 0,\
                "Should return zero if are equal with different length [case 1]"

        def test_versions_different_length_equals_case2(self):
            assert compare_versions(' 1.2.3.0.0.1.0', '1.2.3.0.0.1.0.0.0') == 0,\
                "Should return zero if are equal with different length [case 2]"

        def test_should_raise_error_if_not_string_parameter(self):
            with pytest.raises(AttributeError):
                compare_versions('1', 2.5)

        def test_should_raise_error_if_unexpected_character(self):
            with pytest.raises(ValueError):
                compare_versions('1.2.c', '1.b.1.a')

    class TestPrepareComparisonResult:
        def test_versions_comparison_result_string_case1(self):
            assert prepare_comparison_result('1.2.3', '1.2.3') == "'1.2.3' is equal to '1.2.3'"

        def test_versions_comparison_result_string_case2(self):
            assert prepare_comparison_result('1', '5') == "'1' is smaller than '5'"

        def test_versions_comparison_result_string_case3(self):
            assert prepare_comparison_result(
                '1.2.3.0.0.1.0', '1.2.3.0.0.1.0.0.0'
            ) == "'1.2.3.0.0.1.0' is equal to '1.2.3.0.0.1.0.0.0'"

        def test_versions_comparison_result_string_case4(self):
            assert prepare_comparison_result('1.2.3.0.0.0.0.0.0', '1.2.3') == "'1.2.3.0.0.0.0.0.0' is equal to '1.2.3'"

        def test_versions_comparison_result_string_case5(self):
            assert prepare_comparison_result('1.0', '5.9.8.5.2') == "'1.0' is smaller than '5.9.8.5.2'"

        def test_versions_comparison_result_string_case6(self):
            assert prepare_comparison_result(
                '1.4.0.6.0.0', '1.4.1.0.0.9.0.5'
            ) == "'1.4.0.6.0.0' is smaller than '1.4.1.0.0.9.0.5'"

        def test_versions_comparison_result_string_case7(self):
            assert prepare_comparison_result(
                '1.2.0.2.2.3.5.7.1', '1.2.1.0.0.1'
            ) == "'1.2.0.2.2.3.5.7.1' is smaller than '1.2.1.0.0.1'"

        def test_versions_comparison_result_string_case8(self):
            assert prepare_comparison_result('5', '1.0.0.0.0') == "'5' is greater than '1.0.0.0.0'"

        def test_versions_comparison_result_string_case9(self):
            assert prepare_comparison_result(
                '1.4.1.0.0.0.0.0.0', '1.4.0.6'
            ) == "'1.4.1.0.0.0.0.0.0' is greater than '1.4.0.6'"

        def test_versions_comparison_result_string_case9(self):
            assert prepare_comparison_result(
                '1.2.1.0.0.0.1', '1.2.0.2.9.0.1.2.1.2.3.5'
            ) == "'1.2.1.0.0.0.1' is greater than '1.2.0.2.9.0.1.2.1.2.3.5'"

        def test_versions_comparison_result_string_case10(self):
            assert prepare_comparison_result('1.4.0.6', '1.4.1.0') == "'1.4.0.6' is smaller than '1.4.1.0'"

        def test_versions_comparison_result_string_case11(self):
            assert prepare_comparison_result('1.2.0', '1.2.1') == "'1.2.0' is smaller than '1.2.1'"

        def test_versions_comparison_result_string_case12(self):
            assert prepare_comparison_result('5', '1') == "'5' is greater than '1'"

        def test_versions_comparison_result_string_case13(self):
            assert prepare_comparison_result('1.4.1.0', '1.4.0.6') == "'1.4.1.0' is greater than '1.4.0.6'"

        def test_versions_comparison_result_string_case14(self):
            assert prepare_comparison_result('1.2.1', '1.2.0') == "'1.2.1' is greater than '1.2.0'"

        def test_versions_comparison_result_string_case15(self):
            with pytest.raises(AttributeError):
                prepare_comparison_result('1', 2.5)

        def test_versions_comparison_result_string_case16(self):
            with pytest.raises(ValueError):
                prepare_comparison_result('1.2.c', '1.b.1.a')
