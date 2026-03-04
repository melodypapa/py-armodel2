"""EthernetPriorityRegeneration AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 128)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.referrable import (
    Referrable,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.referrable import ReferrableBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class EthernetPriorityRegeneration(Referrable):
    """AUTOSAR EthernetPriorityRegeneration."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "ETHERNET-PRIORITY-REGENERATION"


    ingress_priority: Optional[PositiveInteger]
    regenerated: Optional[PositiveInteger]
    _DESERIALIZE_DISPATCH = {
        "INGRESS-PRIORITY": lambda obj, elem: setattr(obj, "ingress_priority", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
        "REGENERATED": lambda obj, elem: setattr(obj, "regenerated", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
    }


    def __init__(self) -> None:
        """Initialize EthernetPriorityRegeneration."""
        super().__init__()
        self.ingress_priority: Optional[PositiveInteger] = None
        self.regenerated: Optional[PositiveInteger] = None

    def serialize(self) -> ET.Element:
        """Serialize EthernetPriorityRegeneration to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(EthernetPriorityRegeneration, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize ingress_priority
        if self.ingress_priority is not None:
            serialized = SerializationHelper.serialize_item(self.ingress_priority, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("INGRESS-PRIORITY")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize regenerated
        if self.regenerated is not None:
            serialized = SerializationHelper.serialize_item(self.regenerated, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("REGENERATED")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "EthernetPriorityRegeneration":
        """Deserialize XML element to EthernetPriorityRegeneration object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized EthernetPriorityRegeneration object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(EthernetPriorityRegeneration, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "INGRESS-PRIORITY":
                setattr(obj, "ingress_priority", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))
            elif tag == "REGENERATED":
                setattr(obj, "regenerated", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))

        return obj



class EthernetPriorityRegenerationBuilder(ReferrableBuilder):
    """Builder for EthernetPriorityRegeneration with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: EthernetPriorityRegeneration = EthernetPriorityRegeneration()


    def with_ingress_priority(self, value: Optional[PositiveInteger]) -> "EthernetPriorityRegenerationBuilder":
        """Set ingress_priority attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.ingress_priority = value
        return self

    def with_regenerated(self, value: Optional[PositiveInteger]) -> "EthernetPriorityRegenerationBuilder":
        """Set regenerated attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.regenerated = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "ingressPriority",
        "regenerated",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> EthernetPriorityRegeneration:
        """Build and return the EthernetPriorityRegeneration instance with validation."""
        self._validate_instance()
        return self._obj