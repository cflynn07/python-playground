import unittest

import flask
import helper

class HelperMakePublicTaskTest(unittest.TestCase):
  def setUp(self):
    self.task = {
      'id': 12345
    }
    self.orig_url_for = flask.url_for
    def monkey_patch_url_for(function, task_id, _external):
      return 'monkey-patched-response'
    helper.url_for = monkey_patch_url_for

  def tearDown(self):
    helper.url_for = self.orig_url_for

  def runTest(self):
    result = helper.make_public_task(self.task)
    print(result)
    # Method should return new object
    self.assertIsNot(id(self.task), id(result))
    self.assertEqual(result['uri'], 'monkey-patched-response')

if __name__ == '__main__':
  unittest.main()
