def compare_versions(version1: str, version2: str) -> int:
	"""Compare 2 version strings

	:param version1: Version string; dot separated numbers;
	:param version2: Version string; dot separated numbers;

	:return:
	positive number: If the first version is greater than the second
	negative number: If the first version is smaller than the second
	zero: If the versions are equals
	"""
	version1, version2 = (map(int, v.split('.')) for v in [version1, version2])
	version1, version2 = zip(*map(lambda grp1, grp2: (grp1 or 0, grp2 or 0), version1, version2))

	for i in range(len(version1)):
		if version1[i] != version2[i]:
			return version1[i] - version2[i]
	return 0


def prepare_comparison_result(version1: str, version2: str) -> str:
	"""Compare 2 version strings and Returns the result in either of three selected pre-formated strings

	:param version1: Version string; dot separated numbers;
	:param version2: Version string; dot separated numbers;

	:return:
	'{version1}' is equal to '{version2}': If the comparison returns 0
	'{version1}' is smaller than '{version2}': If the comparison returns -1
	'{version1}' is greater than '{version2}': If the comparison returns 1
	"""
	answer = compare_versions(version1, version2)

	result = f"'{version1}' is equal to '{version2}'"
	if answer < 0:
		result = f"'{version1}' is smaller than '{version2}'"
	elif answer > 0:
		result = f"'{version1}' is greater than '{version2}'"

	return result
