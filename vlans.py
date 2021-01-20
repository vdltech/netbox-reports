from ipam.models import VLAN
from extras.reports import Report
from django.db.models import Q

class VLANMemberReport(Report):
  description = 'Validate that all VLANs have at least one member'

  def test_vlan_has_members(self):
    for vlan in VLAN.objects.all():
      members_count = vlan.get_interfaces().count()
      if members_count == 0:
        self.log_failure(vlan, "has no members")
      else:
        self.log_success(vlan, "has {} members".format(members_count))
