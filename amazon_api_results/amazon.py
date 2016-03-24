from amazon.api import AmazonAPI

amazon = AmazonAPI("AKIAIVHGCP277VB46DMA", "2JYi7rAHq5cGbKN6ISTL96HaPRpqoVODUsUSH93F", "libra0c8-21")
products = amazon.similarity_lookup(ItemId='B0051QVESA,B005DOK8NW')
print products