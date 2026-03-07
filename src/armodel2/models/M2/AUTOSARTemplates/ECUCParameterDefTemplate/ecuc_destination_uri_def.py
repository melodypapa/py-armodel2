"""EcucDestinationUriDef AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 82)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_ECUCParameterDefTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import IdentifiableBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class EcucDestinationUriDef(Identifiable):
    """AUTOSAR EcucDestinationUriDef."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "ECUC-DESTINATION-URI-DEF"


    destination_uri: Optional[Any]
    _DESERIALIZE_DISPATCH = {
        "DESTINATION-URI": lambda obj, elem: setattr(obj, "destination_uri", SerializationHelper.deserialize_by_tag(elem, "any (EcucDestinationUri)")),
    }


    def __init__(self) -> None:
        """Initialize EcucDestinationUriDef."""
        super().__init__()
        self.destination_uri: Optional[Any] = None

    def serialize(self) -> ET.Element:
        """Serialize EcucDestinationUriDef to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(EcucDestinationUriDef, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize destination_uri
        if self.destination_uri is not None:
            serialized = SerializationHelper.serialize_item(self.destination_uri, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DESTINATION-URI")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "EcucDestinationUriDef":
        """Deserialize XML element to EcucDestinationUriDef object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized EcucDestinationUriDef object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(EcucDestinationUriDef, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "DESTINATION-URI":
                setattr(obj, "destination_uri", SerializationHelper.deserialize_by_tag(child, "any (EcucDestinationUri)"))

        return obj



class EcucDestinationUriDefBuilder(IdentifiableBuilder):
    """Builder for EcucDestinationUriDef with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: EcucDestinationUriDef = EcucDestinationUriDef()


    def with_destination_uri(self, value: Optional[Any]) -> "EcucDestinationUriDefBuilder":
        """Set destination_uri attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'destination_uri' is required and cannot be None")
        self._obj.destination_uri = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "destinationUri",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> EcucDestinationUriDef:
        """Build and return the EcucDestinationUriDef instance with validation."""
        self._validate_instance()
        return self._obj