"""SwitchStreamFilterActionDestPortModification AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 140)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import IdentifiableBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.coupling_port import (
    CouplingPort,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class SwitchStreamFilterActionDestPortModification(Identifiable):
    """AUTOSAR SwitchStreamFilterActionDestPortModification."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "SWITCH-STREAM-FILTER-ACTION-DEST-PORT-MODIFICATION"


    egress_port_refs: list[ARRef]
    modification: Optional[Any]
    _DESERIALIZE_DISPATCH = {
        "EGRESS-PORT-REFS": lambda obj, elem: [obj.egress_port_refs.append(ARRef.deserialize(item_elem)) for item_elem in elem],
        "MODIFICATION": lambda obj, elem: setattr(obj, "modification", SerializationHelper.deserialize_by_tag(elem, "any (SwitchStreamFilter)")),
    }


    def __init__(self) -> None:
        """Initialize SwitchStreamFilterActionDestPortModification."""
        super().__init__()
        self.egress_port_refs: list[ARRef] = []
        self.modification: Optional[Any] = None

    def serialize(self) -> ET.Element:
        """Serialize SwitchStreamFilterActionDestPortModification to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(SwitchStreamFilterActionDestPortModification, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize egress_port_refs (list to container "EGRESS-PORT-REFS")
        if self.egress_port_refs:
            wrapper = ET.Element("EGRESS-PORT-REFS")
            for item in self.egress_port_refs:
                serialized = SerializationHelper.serialize_item(item, "CouplingPort")
                if serialized is not None:
                    child_elem = ET.Element("EGRESS-PORT-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize modification
        if self.modification is not None:
            serialized = SerializationHelper.serialize_item(self.modification, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MODIFICATION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SwitchStreamFilterActionDestPortModification":
        """Deserialize XML element to SwitchStreamFilterActionDestPortModification object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SwitchStreamFilterActionDestPortModification object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(SwitchStreamFilterActionDestPortModification, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "EGRESS-PORT-REFS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.egress_port_refs.append(ARRef.deserialize(item_elem))
            elif tag == "MODIFICATION":
                setattr(obj, "modification", SerializationHelper.deserialize_by_tag(child, "any (SwitchStreamFilter)"))

        return obj



class SwitchStreamFilterActionDestPortModificationBuilder(IdentifiableBuilder):
    """Builder for SwitchStreamFilterActionDestPortModification with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: SwitchStreamFilterActionDestPortModification = SwitchStreamFilterActionDestPortModification()


    def with_egress_ports(self, items: list[CouplingPort]) -> "SwitchStreamFilterActionDestPortModificationBuilder":
        """Set egress_ports list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.egress_ports = list(items) if items else []
        return self

    def with_modification(self, value: Optional[any (SwitchStreamFilter)]) -> "SwitchStreamFilterActionDestPortModificationBuilder":
        """Set modification attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.modification = value
        return self


    def add_egress_port(self, item: CouplingPort) -> "SwitchStreamFilterActionDestPortModificationBuilder":
        """Add a single item to egress_ports list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.egress_ports.append(item)
        return self

    def clear_egress_ports(self) -> "SwitchStreamFilterActionDestPortModificationBuilder":
        """Clear all items from egress_ports list.

        Returns:
            self for method chaining
        """
        self._obj.egress_ports = []
        return self


    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "egressPort",
        "modification",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> SwitchStreamFilterActionDestPortModification:
        """Build and return the SwitchStreamFilterActionDestPortModification instance with validation."""
        self._validate_instance()
        return self._obj