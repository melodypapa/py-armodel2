"""DoIpLogicTesterAddressProps AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 556)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_DoIP.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.DoIP.abstract_do_ip_logic_address_props import (
    AbstractDoIpLogicAddressProps,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.DoIP.do_ip_routing_activation import (
    DoIpRoutingActivation,
)


class DoIpLogicTesterAddressProps(AbstractDoIpLogicAddressProps):
    """AUTOSAR DoIpLogicTesterAddressProps."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    do_ip_testers: list[DoIpRoutingActivation]
    def __init__(self) -> None:
        """Initialize DoIpLogicTesterAddressProps."""
        super().__init__()
        self.do_ip_testers: list[DoIpRoutingActivation] = []
    def serialize(self) -> ET.Element:
        """Serialize DoIpLogicTesterAddressProps to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = ARObject._get_xml_tag(self)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DoIpLogicTesterAddressProps, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize do_ip_testers (list to container "DO-IP-TESTERS")
        if self.do_ip_testers:
            wrapper = ET.Element("DO-IP-TESTERS")
            for item in self.do_ip_testers:
                serialized = ARObject._serialize_item(item, "DoIpRoutingActivation")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DoIpLogicTesterAddressProps":
        """Deserialize XML element to DoIpLogicTesterAddressProps object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DoIpLogicTesterAddressProps object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DoIpLogicTesterAddressProps, cls).deserialize(element)

        # Parse do_ip_testers (list from container "DO-IP-TESTERS")
        obj.do_ip_testers = []
        container = ARObject._find_child_element(element, "DO-IP-TESTERS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.do_ip_testers.append(child_value)

        return obj



class DoIpLogicTesterAddressPropsBuilder:
    """Builder for DoIpLogicTesterAddressProps."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DoIpLogicTesterAddressProps = DoIpLogicTesterAddressProps()

    def build(self) -> DoIpLogicTesterAddressProps:
        """Build and return DoIpLogicTesterAddressProps object.

        Returns:
            DoIpLogicTesterAddressProps instance
        """
        # TODO: Add validation
        return self._obj
