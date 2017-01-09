from shutit_module import ShutItModule

class shutit_cookbook_openshift3_test(ShutItModule):


	def build(self, shutit):
		shutit.pause_point('kitchen')
		return True

def module():
		return shutit_cookbook_openshift3_test(
			'git.shutit_cookbook_openshift3_test.shutit_cookbook_openshift3_test', 19404428.0001,
			description='',
			maintainer='',
			delivery_methods=['bash'],
			depends=['shutit-library.chefdk.chefdk']
		)
