"""BuildEngineeringObject AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 372)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_GenericStructure_BuildActionManifest.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.EngineeringObject.engineering_object import (
    EngineeringObject,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.EngineeringObject.engineering_object import EngineeringObjectBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    NameToken,
    RegularExpression,
    UriString,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class BuildEngineeringObject(EngineeringObject):
    """AUTOSAR BuildEngineeringObject."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "BUILD-ENGINEERING-OBJECT"


    file_type: NameToken
    file_type_pattern: RegularExpression
    intended: Optional[UriString]
    _DESERIALIZE_DISPATCH = {
        "FILE-TYPE": lambda obj, elem: setattr(obj, "file_type", SerializationHelper.deserialize_by_tag(elem, "NameToken")),
        "FILE-TYPE-PATTERN": lambda obj, elem: setattr(obj, "file_type_pattern", SerializationHelper.deserialize_by_tag(elem, "RegularExpression")),
        "INTENDED": lambda obj, elem: setattr(obj, "intended", SerializationHelper.deserialize_by_tag(elem, "UriString")),
    }


    def __init__(self) -> None:
        """Initialize BuildEngineeringObject."""
        super().__init__()
        self.file_type: NameToken = None
        self.file_type_pattern: RegularExpression = None
        self.intended: Optional[UriString] = None

    def serialize(self) -> ET.Element:
        """Serialize BuildEngineeringObject to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(BuildEngineeringObject, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize file_type
        if self.file_type is not None:
            serialized = SerializationHelper.serialize_item(self.file_type, "NameToken")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("FILE-TYPE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize file_type_pattern
        if self.file_type_pattern is not None:
            serialized = SerializationHelper.serialize_item(self.file_type_pattern, "RegularExpression")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("FILE-TYPE-PATTERN")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize intended
        if self.intended is not None:
            serialized = SerializationHelper.serialize_item(self.intended, "UriString")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("INTENDED")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "BuildEngineeringObject":
        """Deserialize XML element to BuildEngineeringObject object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized BuildEngineeringObject object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(BuildEngineeringObject, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "FILE-TYPE":
                setattr(obj, "file_type", SerializationHelper.deserialize_by_tag(child, "NameToken"))
            elif tag == "FILE-TYPE-PATTERN":
                setattr(obj, "file_type_pattern", SerializationHelper.deserialize_by_tag(child, "RegularExpression"))
            elif tag == "INTENDED":
                setattr(obj, "intended", SerializationHelper.deserialize_by_tag(child, "UriString"))

        return obj



class BuildEngineeringObjectBuilder(EngineeringObjectBuilder):
    """Builder for BuildEngineeringObject with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: BuildEngineeringObject = BuildEngineeringObject()


    def with_file_type(self, value: NameToken) -> "BuildEngineeringObjectBuilder":
        """Set file_type attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not False:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.file_type = value
        return self

    def with_file_type_pattern(self, value: RegularExpression) -> "BuildEngineeringObjectBuilder":
        """Set file_type_pattern attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not False:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.file_type_pattern = value
        return self

    def with_intended(self, value: Optional[UriString]) -> "BuildEngineeringObjectBuilder":
        """Set intended attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.intended = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _REQUIRED_ATTRIBUTES = {
        "fileType",
        "fileTypePattern",
    }
    _OPTIONAL_ATTRIBUTES = {
        "intended",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # Validate required attributes using pre-computed constants (O(1) lookup)
        # This is much faster than calling get_type_hints() at runtime
        if getattr(self._obj, "fileType", None) is None:
            if mode == BuilderValidationMode.STRICT:
                raise ValueError("Required attribute 'fileType' is None")
            elif mode == BuilderValidationMode.LENIENT:
                import warnings
                warnings.warn("Required attribute 'fileType' is None", UserWarning)
        if getattr(self._obj, "fileTypePattern", None) is None:
            if mode == BuilderValidationMode.STRICT:
                raise ValueError("Required attribute 'fileTypePattern' is None")
            elif mode == BuilderValidationMode.LENIENT:
                import warnings
                warnings.warn("Required attribute 'fileTypePattern' is None", UserWarning)


    def build(self) -> BuildEngineeringObject:
        """Build and return the BuildEngineeringObject instance with validation."""
        self._validate_instance()
        return self._obj