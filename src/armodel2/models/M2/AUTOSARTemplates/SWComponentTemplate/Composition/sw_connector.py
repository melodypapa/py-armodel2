"""SwConnector AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 307)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 80)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2061)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_Composition.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import IdentifiableBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.port_interface_mapping import (
    PortInterfaceMapping,
)
from abc import ABC, abstractmethod
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class SwConnector(Identifiable, ABC):
    """AUTOSAR SwConnector."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    mapping_ref: Optional[ARRef]
    _DESERIALIZE_DISPATCH = {
        "MAPPING-REF": ("_POLYMORPHIC", "mapping_ref", ["ClientServerInterfaceMapping", "ModeInterfaceMapping", "TriggerInterfaceMapping", "VariableAndParameter"]),
    }


    def __init__(self) -> None:
        """Initialize SwConnector."""
        super().__init__()
        self.mapping_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize SwConnector to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(SwConnector, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize mapping_ref
        if self.mapping_ref is not None:
            serialized = SerializationHelper.serialize_item(self.mapping_ref, "PortInterfaceMapping")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MAPPING-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SwConnector":
        """Deserialize XML element to SwConnector object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SwConnector object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(SwConnector, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "MAPPING-REF":
                setattr(obj, "mapping_ref", ARRef.deserialize(child))

        return obj



class SwConnectorBuilder(IdentifiableBuilder):
    """Builder for SwConnector with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: SwConnector = SwConnector()


    def with_mapping(self, value: Optional[PortInterfaceMapping]) -> "SwConnectorBuilder":
        """Set mapping attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.mapping = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "mapping",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    @abstractmethod
    def build(self) -> SwConnector:
        """Build and return the SwConnector instance (abstract)."""
        raise NotImplementedError