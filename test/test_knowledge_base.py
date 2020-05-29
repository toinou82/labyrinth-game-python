import unittest
import impl.knowledge_base as kb


class TestKnowledgeBase(unittest.TestCase):

    def test_find_obj(self):
        knowledge_base = kb.KnowledgeBase(kb.make_objects_dict())
        prime = kb.GenericMathObject("Prime", "Prime  number")
        base_prime1 = knowledge_base.find_obj("Prime")
        self.assertEqual(prime.get_name(), base_prime1.get_name())

    def test_find_obj2(self):
        knowledge_base = kb.KnowledgeBase(kb.make_objects_dict())
        base_prime1 = knowledge_base.find_obj("Prime")
        base_prime2 = knowledge_base.find_obj("Prime")

        self.assertEqual(base_prime1, base_prime2)

    def test_find_obj_not_found(self):
        knowledge_base = kb.KnowledgeBase(kb.make_objects_dict())
        base_prime2 = knowledge_base.find_obj("caca")
        print(base_prime2)

    def test_add_obj(self):
        knowledge_base = kb.KnowledgeBase(kb.make_objects_dict())
        knowledge_base.aj_obj("my_new_obj", "my_new_desc")
        obj = knowledge_base.find_obj("my_new_obj")
        self.assertEqual(type(obj), kb.GenericMathObject)
        self.assertEqual(obj.get_name(), "my_new_obj")
        self.assertEqual(obj.get_description(), "my_new_desc")

if __name__ == '__main__':
    unittest.main()