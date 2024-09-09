import random


def dot(A, B):
    return (sum(a * b for a, b in zip(A, B)))


def cosine(nums1, nums2):
    return dot(nums1, nums2) / ((dot(nums1, nums1) ** .5) * (dot(nums2, nums2) ** .5))


nums1 = [random.randint(0, 20) for _ in range(4)]
nums2 = [random.randint(0, 20) for _ in range(4)]
print('Список A:', nums1)
print('Список B:', nums2)

result = cosine(nums1, nums2)
print('Результат:', result)
