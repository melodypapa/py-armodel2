"""DoIpLogicTesterAddressProps AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 556)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_DoIP.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.DoIP.abstract_do_ip_logic_address_props import (
    AbstractDoIpLogicAddressProps,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.DoIP.abstract_do_ip_logic_address_props import AbstractDoIpLogicAddressPropsBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.DoIP.do_ip_routing_activation import (
    DoIpRoutingActivation,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class DoIpLogicTesterAddressProps(AbstractDoIpLogicAddressProps):
    """AUTOSAR DoIpLogicTesterAddressProps."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "DO-IP-LOGIC-TESTER-ADDRESS-PROPS"


    do_ip_tester_refs: list[ARRef]
    _DESERIALIZE_DISPATCH = {
        "DO-IP-TESTER-REFS": lambda obj, elem: [obj.do_ip_tester_refs.append(ARRef.deserialize(item_elem)) for item_elem in elem],
    }


    def __init__(self) -> None:
        """Initialize DoIpLogicTesterAddressProps."""
        super().__init__()
        self.do_ip_tester_refs: list[ARRef] = []

    def serialize(self) -> ET.Element:
        """Serialize DoIpLogicTesterAddressProps to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DoIpLogicTesterAddressProps, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize do_ip_tester_refs (list to container "DO-IP-TESTER-REFS")
        if self.do_ip_tester_refs:
            wrapper = ET.Element("DO-IP-TESTER-REFS")
            for item in self.do_ip_tester_refs:
                serialized = SerializationHelper.serialize_item(item, "DoIpRoutingActivation")
                if serialized is not None:
                    child_elem = ET.Element("DO-IP-TESTER-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
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

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "DO-IP-TESTER-REFS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.do_ip_tester_refs.append(ARRef.deserialize(item_elem))

        return obj



class DoIpLogicTesterAddressPropsBuilder(AbstractDoIpLogicAddressPropsBuilder):
    """Builder for DoIpLogicTesterAddressProps with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: DoIpLogicTesterAddressProps = DoIpLogicTesterAddressProps()


    def with_do_ip_testers(self, items: list[DoIpRoutingActivation]) -> "DoIpLogicTesterAddressPropsBuilder":
        """Set do_ip_testers list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.do_ip_testers = list(items) if items else []
        return self


    def add_do_ip_tester(self, item: DoIpRoutingActivation) -> "DoIpLogicTesterAddressPropsBuilder":
        """Add a single item to do_ip_testers list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.do_ip_testers.append(item)
        return self

    def clear_do_ip_testers(self) -> "DoIpLogicTesterAddressPropsBuilder":
        """Clear all items from do_ip_testers list.

        Returns:
            self for method chaining
        """
        self._obj.do_ip_testers = []
        return self


    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "doIpTester",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> DoIpLogicTesterAddressProps:
        """Build and return the DoIpLogicTesterAddressProps instance with validation."""
        self._validate_instance()
        return self._obj