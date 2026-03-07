"""ApplicationRecordElement AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 261)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 1997)
  - AUTOSAR_FO_TPS_AbstractPlatformSpecification.pdf (page 43)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_Datatype_DataPrototypes.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.application_composite_element_data_prototype import (
    ApplicationCompositeElementDataPrototype,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.application_composite_element_data_prototype import ApplicationCompositeElementDataPrototypeBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class ApplicationRecordElement(ApplicationCompositeElementDataPrototype):
    """AUTOSAR ApplicationRecordElement."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "APPLICATION-RECORD-ELEMENT"


    is_optional: Optional[Boolean]
    _DESERIALIZE_DISPATCH = {
        "IS-OPTIONAL": lambda obj, elem: setattr(obj, "is_optional", SerializationHelper.deserialize_by_tag(elem, "Boolean")),
    }


    def __init__(self) -> None:
        """Initialize ApplicationRecordElement."""
        super().__init__()
        self.is_optional: Optional[Boolean] = None

    def serialize(self) -> ET.Element:
        """Serialize ApplicationRecordElement to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(ApplicationRecordElement, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize is_optional
        if self.is_optional is not None:
            serialized = SerializationHelper.serialize_item(self.is_optional, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("IS-OPTIONAL")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ApplicationRecordElement":
        """Deserialize XML element to ApplicationRecordElement object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ApplicationRecordElement object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(ApplicationRecordElement, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "IS-OPTIONAL":
                setattr(obj, "is_optional", SerializationHelper.deserialize_by_tag(child, "Boolean"))

        return obj



class ApplicationRecordElementBuilder(ApplicationCompositeElementDataPrototypeBuilder):
    """Builder for ApplicationRecordElement with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: ApplicationRecordElement = ApplicationRecordElement()


    def with_is_optional(self, value: Optional[Boolean]) -> "ApplicationRecordElementBuilder":
        """Set is_optional attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'is_optional' is required and cannot be None")
        self._obj.is_optional = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "isOptional",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> ApplicationRecordElement:
        """Build and return the ApplicationRecordElement instance with validation."""
        self._validate_instance()
        return self._obj