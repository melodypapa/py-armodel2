"""DoIpRoutingActivation AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 553)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_DoIP.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import IdentifiableBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.DoIP.do_ip_logic_target_address_props import (
    DoIpLogicTargetAddressProps,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class DoIpRoutingActivation(Identifiable):
    """AUTOSAR DoIpRoutingActivation."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "DO-IP-ROUTING-ACTIVATION"


    do_ip_target_refs: list[ARRef]
    _DESERIALIZE_DISPATCH = {
        "DO-IP-TARGET-REFS": lambda obj, elem: [obj.do_ip_target_refs.append(ARRef.deserialize(item_elem)) for item_elem in elem],
    }


    def __init__(self) -> None:
        """Initialize DoIpRoutingActivation."""
        super().__init__()
        self.do_ip_target_refs: list[ARRef] = []

    def serialize(self) -> ET.Element:
        """Serialize DoIpRoutingActivation to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DoIpRoutingActivation, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize do_ip_target_refs (list to container "DO-IP-TARGET-REFS")
        if self.do_ip_target_refs:
            wrapper = ET.Element("DO-IP-TARGET-REFS")
            for item in self.do_ip_target_refs:
                serialized = SerializationHelper.serialize_item(item, "DoIpLogicTargetAddressProps")
                if serialized is not None:
                    child_elem = ET.Element("DO-IP-TARGET-REF")
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
    def deserialize(cls, element: ET.Element) -> "DoIpRoutingActivation":
        """Deserialize XML element to DoIpRoutingActivation object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DoIpRoutingActivation object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DoIpRoutingActivation, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "DO-IP-TARGET-REFS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.do_ip_target_refs.append(ARRef.deserialize(item_elem))

        return obj



class DoIpRoutingActivationBuilder(IdentifiableBuilder):
    """Builder for DoIpRoutingActivation with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: DoIpRoutingActivation = DoIpRoutingActivation()


    def with_do_ip_targets(self, items: list[DoIpLogicTargetAddressProps]) -> "DoIpRoutingActivationBuilder":
        """Set do_ip_targets list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.do_ip_targets = list(items) if items else []
        return self


    def add_do_ip_target(self, item: DoIpLogicTargetAddressProps) -> "DoIpRoutingActivationBuilder":
        """Add a single item to do_ip_targets list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.do_ip_targets.append(item)
        return self

    def clear_do_ip_targets(self) -> "DoIpRoutingActivationBuilder":
        """Clear all items from do_ip_targets list.

        Returns:
            self for method chaining
        """
        self._obj.do_ip_targets = []
        return self


    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "doIpTarget",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> DoIpRoutingActivation:
        """Build and return the DoIpRoutingActivation instance with validation."""
        self._validate_instance()
        return self._obj