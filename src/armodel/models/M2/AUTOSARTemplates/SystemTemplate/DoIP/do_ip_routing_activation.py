"""DoIpRoutingActivation AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 553)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_DoIP.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.DoIP.do_ip_logic_target_address_props import (
    DoIpLogicTargetAddressProps,
)


class DoIpRoutingActivation(Identifiable):
    """AUTOSAR DoIpRoutingActivation."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    do_ip_targets: list[DoIpLogicTargetAddressProps]
    def __init__(self) -> None:
        """Initialize DoIpRoutingActivation."""
        super().__init__()
        self.do_ip_targets: list[DoIpLogicTargetAddressProps] = []
    def serialize(self) -> ET.Element:
        """Serialize DoIpRoutingActivation to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DoIpRoutingActivation, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize do_ip_targets (list to container "DO-IP-TARGETS")
        if self.do_ip_targets:
            wrapper = ET.Element("DO-IP-TARGETS")
            for item in self.do_ip_targets:
                serialized = ARObject._serialize_item(item, "DoIpLogicTargetAddressProps")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DoIpRoutingActivation":
        """Deserialize XML element to DoIpRoutingActivation object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DoIpRoutingActivation object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DoIpRoutingActivation, cls).deserialize(element)

        # Parse do_ip_targets (list from container "DO-IP-TARGETS")
        obj.do_ip_targets = []
        container = ARObject._find_child_element(element, "DO-IP-TARGETS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.do_ip_targets.append(child_value)

        return obj



class DoIpRoutingActivationBuilder:
    """Builder for DoIpRoutingActivation."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DoIpRoutingActivation = DoIpRoutingActivation()

    def build(self) -> DoIpRoutingActivation:
        """Build and return DoIpRoutingActivation object.

        Returns:
            DoIpRoutingActivation instance
        """
        # TODO: Add validation
        return self._obj
