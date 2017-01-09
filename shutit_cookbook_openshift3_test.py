from shutit_module import ShutItModule
import random
import string

class shutit_cookbook_openshift3_test(ShutItModule):


	def build(self, shutit):
		rnd = ''.join(random.choice(string.ascii_letters) for _ in range(6))
		shutit.send('mkdir -p /tmp/shutit_cookbook_openshift3_test_' + rnd)
		shutit.send('pushd /tmp/shutit_cookbook_openshift3_test_' + rnd)
		shutit.send('git clone https://github.com/IshentRas/cookbook-openshift3')
		shutit.send('pushd cookbook-openshift3')
		shutit.pause_point('kitchen')
		shutit.send('popd')
		shutit.send('popd')
		shutit.send('rm -rf /tmp/shutit_cookbook_openshift3_test_' + rnd)
		return True

def module():
		return shutit_cookbook_openshift3_test(
			'tk.shutit.shutit_cookbook_openshift3_test.shutit_cookbook_openshift3_test', 19404428.0001,
			description='',
			maintainer='',
			delivery_methods=['bash'],
			depends=['shutit-library.inspec.inspec']
		)
