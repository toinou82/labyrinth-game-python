import unittest
from impl.commands import Add
import impl.knowledge_base as kb


class TestCommands(unittest.TestCase):

    def test_add_get_command_tag(self):
        add_command = Ajouter()
        self.assertEqual(add_command.get_command_tag(), "add")

    def test_add_get_args_count(self):
        add_command = Ajouter()
        self.assertEqual(add_command.get_args_count(), 2)

    def test_add_evaluate(self):
        add_command = Ajouter()
        base = kb.KnowledgeBase(kb.make_objects_dict())
        cont, state, message = add_command.evaluate("", ["obj_name", "obj_desc"], base)
        self.assertEqual(cont, False)
        self.assertEqual(state, "")
        self.assertEqual(message, "Successfully added the object : obj_name / obj_desc")
        self.assertEqual(base.find_obj("obj_name").get_description(), "obj_desc")

    def test_add_evaluate_already_exist(self):
        add_command = Ajouter()
        base = kb.KnowledgeBase(kb.make_objects_dict())
        cont, state, message = add_command.evaluate("", ["obj_name", "obj_desc"], base)
        self.assertEqual(cont, False)
        self.assertEqual(state, "")
        self.assertEqual(message, "Successfully added the object : obj_name / obj_desc")

        cont, state, message = add_command.evaluate("", ["obj_name", "obj_desc"], base)
        self.assertEqual(cont, False)
        self.assertEqual(state, "")
        self.assertEqual(message, "Object already in DB")

    def test_add_evaluate_invalid_args(self):
        add_command = Ajouter()
        base = kb.KnowledgeBase(kb.make_objects_dict())

        with self.assertRaises(Exception) as context:
            add_command.evaluate("", ["obj_name"], base)

        self.assertTrue('Invalid number of arguments : add NAME DESCRIPTION' in str(context.exception))


if __name__ == '__main__':
    unittest.main()