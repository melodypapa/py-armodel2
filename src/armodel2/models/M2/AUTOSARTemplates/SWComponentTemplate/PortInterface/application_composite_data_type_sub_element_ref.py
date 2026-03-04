"""ApplicationCompositeDataTypeSubElementRef AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 138)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_PortInterface.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.sub_element_ref import (
    SubElementRef,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.sub_element_ref import SubElementRefBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class ApplicationCompositeDataTypeSubElementRef(SubElementRef):
    """AUTOSAR ApplicationCompositeDataTypeSubElementRef."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "APPLICATION-COMPOSITE-DATA-TYPE-SUB-ELEMENT-REF"


    application: Optional[Any]
    _DESERIALIZE_DISPATCH = {
        "APPLICATION": lambda obj, elem: setattr(obj, "application", SerializationHelper.deserialize_by_tag(elem, "any (ApplicationComposite)")),
    }


    def __init__(self) -> None:
        """Initialize ApplicationCompositeDataTypeSubElementRef."""
        super().__init__()
        self.application: Optional[Any] = None

    def serialize(self) -> ET.Element:
        """Serialize ApplicationCompositeDataTypeSubElementRef to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(ApplicationCompositeDataTypeSubElementRef, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize application
        if self.application is not None:
            serialized = SerializationHelper.serialize_item(self.application, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("APPLICATION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ApplicationCompositeDataTypeSubElementRef":
        """Deserialize XML element to ApplicationCompositeDataTypeSubElementRef object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ApplicationCompositeDataTypeSubElementRef object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(ApplicationCompositeDataTypeSubElementRef, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "APPLICATION":
                setattr(obj, "application", SerializationHelper.deserialize_by_tag(child, "any (ApplicationComposite)"))

        return obj



class ApplicationCompositeDataTypeSubElementRefBuilder(SubElementRefBuilder):
    """Builder for ApplicationCompositeDataTypeSubElementRef with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: ApplicationCompositeDataTypeSubElementRef = ApplicationCompositeDataTypeSubElementRef()


    def with_application(self, value: Optional[any (ApplicationComposite)]) -> "ApplicationCompositeDataTypeSubElementRefBuilder":
        """Set application attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.application = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "application",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> ApplicationCompositeDataTypeSubElementRef:
        """Build and return the ApplicationCompositeDataTypeSubElementRef instance with validation."""
        self._validate_instance()
        return self._obj