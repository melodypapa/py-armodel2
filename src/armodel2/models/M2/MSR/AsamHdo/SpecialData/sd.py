"""Sd AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 91)

JSON Source: docs/json/packages/M2_MSR_AsamHdo_SpecialData.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel2.serialization.decorators import xml_attribute

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    NameToken,
    VerbatimStringPlain,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class Sd(ARObject):
    """AUTOSAR Sd."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "SD"


    _gid: NameToken
    value: VerbatimStringPlain
    xml_space: Optional[XmlSpaceEnum]
    _DESERIALIZE_DISPATCH = {
        "VALUE": lambda obj, elem: setattr(obj, "value", SerializationHelper.deserialize_by_tag(elem, "VerbatimStringPlain")),
        "XML-SPACE": lambda obj, elem: setattr(obj, "xml_space", SerializationHelper.deserialize_by_tag(elem, "XmlSpaceEnum")),
    }


    def __init__(self) -> None:
        """Initialize Sd."""
        super().__init__()
        self._gid: NameToken = None
        self.value: VerbatimStringPlain = None
        self.xml_space: Optional[XmlSpaceEnum] = None
    @property
    @xml_attribute
    def gid(self) -> NameToken:
        """Get gid XML attribute."""
        return self._gid

    @gid.setter
    def gid(self, value: NameToken) -> None:
        """Set gid XML attribute."""
        self._gid = value


    def serialize(self) -> ET.Element:
        """Serialize Sd to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(Sd, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize gid as XML attribute
        if self.gid is not None:
            elem.attrib["GID"] = str(self.gid)

        # Serialize value
        if self.value is not None:
            serialized = SerializationHelper.serialize_item(self.value, "VerbatimStringPlain")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("VALUE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize xml_space
        if self.xml_space is not None:
            serialized = SerializationHelper.serialize_item(self.xml_space, "XmlSpaceEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("XML-SPACE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "Sd":
        """Deserialize XML element to Sd object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized Sd object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(Sd, cls).deserialize(element)

        # Parse gid from XML attribute
        if "GID" in element.attrib:
            obj.gid = element.attrib["GID"]

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "VALUE":
                setattr(obj, "value", SerializationHelper.deserialize_by_tag(child, "VerbatimStringPlain"))
            elif tag == "XML-SPACE":
                setattr(obj, "xml_space", SerializationHelper.deserialize_by_tag(child, "XmlSpaceEnum"))

        return obj



class SdBuilder(BuilderBase):
    """Builder for Sd with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: Sd = Sd()


    def with_gid(self, value: NameToken) -> "SdBuilder":
        """Set gid attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not False:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.gid = value
        return self

    def with_value(self, value: VerbatimStringPlain) -> "SdBuilder":
        """Set value attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not False:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.value = value
        return self

    def with_xml_space(self, value: Optional[XmlSpaceEnum]) -> "SdBuilder":
        """Set xml_space attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.xml_space = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _REQUIRED_ATTRIBUTES = {
        "gid",
        "value",
    }
    _OPTIONAL_ATTRIBUTES = {
        "xmlSpace",
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
        if getattr(self._obj, "gid", None) is None:
            if mode == BuilderValidationMode.STRICT:
                raise ValueError("Required attribute 'gid' is None")
            elif mode == BuilderValidationMode.LENIENT:
                import warnings
                warnings.warn("Required attribute 'gid' is None", UserWarning)
        if getattr(self._obj, "value", None) is None:
            if mode == BuilderValidationMode.STRICT:
                raise ValueError("Required attribute 'value' is None")
            elif mode == BuilderValidationMode.LENIENT:
                import warnings
                warnings.warn("Required attribute 'value' is None", UserWarning)


    def build(self) -> Sd:
        """Build and return the Sd instance with validation."""
        self._validate_instance()
        return self._obj