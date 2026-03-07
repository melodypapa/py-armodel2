"""WhitespaceControlled AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 292)

JSON Source: docs/json/packages/M2_MSR_Documentation_TextModel_LanguageDataModel.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from abc import ABC, abstractmethod
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class WhitespaceControlled(ARObject, ABC):
    """AUTOSAR WhitespaceControlled."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    xml_space: Any
    _DESERIALIZE_DISPATCH = {
        "XML-SPACE": lambda obj, elem: setattr(obj, "xml_space", SerializationHelper.deserialize_by_tag(elem, "any (XmlSpaceEnum)")),
    }


    def __init__(self) -> None:
        """Initialize WhitespaceControlled."""
        super().__init__()
        self.xml_space: Any = None

    def serialize(self) -> ET.Element:
        """Serialize WhitespaceControlled to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(WhitespaceControlled, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize xml_space
        if self.xml_space is not None:
            serialized = SerializationHelper.serialize_item(self.xml_space, "Any")
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
    def deserialize(cls, element: ET.Element) -> "WhitespaceControlled":
        """Deserialize XML element to WhitespaceControlled object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized WhitespaceControlled object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(WhitespaceControlled, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "XML-SPACE":
                setattr(obj, "xml_space", SerializationHelper.deserialize_by_tag(child, "any (XmlSpaceEnum)"))

        return obj



class WhitespaceControlledBuilder(BuilderBase, ABC):
    """Builder for WhitespaceControlled with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: WhitespaceControlled = WhitespaceControlled()


    def with_xml_space(self, value: Any) -> "WhitespaceControlledBuilder":
        """Set xml_space attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not False:
            raise ValueError("Attribute 'xml_space' is required and cannot be None")
        self._obj.xml_space = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _REQUIRED_ATTRIBUTES = {
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
        if getattr(self._obj, "xmlSpace", None) is None:
            if mode == BuilderValidationMode.STRICT:
                raise ValueError("Required attribute 'xmlSpace' is None")
            elif mode == BuilderValidationMode.LENIENT:
                import warnings
                warnings.warn("Required attribute 'xmlSpace' is None", UserWarning)


    @abstractmethod
    def build(self) -> WhitespaceControlled:
        """Build and return the WhitespaceControlled instance (abstract)."""
        raise NotImplementedError