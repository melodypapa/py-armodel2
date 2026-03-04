"""SdgElementWithGid AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 99)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_GenericStructure_GeneralTemplateClasses_SpecialDataDef.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    NameToken,
)
from abc import ABC, abstractmethod
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class SdgElementWithGid(ARObject, ABC):
    """AUTOSAR SdgElementWithGid."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    gid: Optional[NameToken]
    _DESERIALIZE_DISPATCH = {
        "GID": lambda obj, elem: setattr(obj, "gid", SerializationHelper.deserialize_by_tag(elem, "NameToken")),
    }


    def __init__(self) -> None:
        """Initialize SdgElementWithGid."""
        super().__init__()
        self.gid: Optional[NameToken] = None

    def serialize(self) -> ET.Element:
        """Serialize SdgElementWithGid to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(SdgElementWithGid, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize gid
        if self.gid is not None:
            serialized = SerializationHelper.serialize_item(self.gid, "NameToken")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("GID")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SdgElementWithGid":
        """Deserialize XML element to SdgElementWithGid object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SdgElementWithGid object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(SdgElementWithGid, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "GID":
                setattr(obj, "gid", SerializationHelper.deserialize_by_tag(child, "NameToken"))

        return obj



class SdgElementWithGidBuilder(BuilderBase, ABC):
    """Builder for SdgElementWithGid with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: SdgElementWithGid = SdgElementWithGid()


    def with_gid(self, value: Optional[NameToken]) -> "SdgElementWithGidBuilder":
        """Set gid attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.gid = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "gid",
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
    def build(self) -> SdgElementWithGid:
        """Build and return the SdgElementWithGid instance (abstract)."""
        raise NotImplementedError