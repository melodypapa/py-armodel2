"""FileInfoComment AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 29)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_AutosarTopLevelStructure.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.MSR.AsamHdo.SpecialData.sdg import (
    Sdg,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class FileInfoComment(ARObject):
    """AUTOSAR FileInfoComment."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "FILE-INFO-COMMENT"


    sdgs: list[Sdg]
    _DESERIALIZE_DISPATCH = {
        "SDGS": lambda obj, elem: obj.sdgs.append(SerializationHelper.deserialize_by_tag(elem, "Sdg")),
    }


    def __init__(self) -> None:
        """Initialize FileInfoComment."""
        super().__init__()
        self.sdgs: list[Sdg] = []

    def serialize(self) -> ET.Element:
        """Serialize FileInfoComment to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(FileInfoComment, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize sdgs (list to container "SDGS")
        if self.sdgs:
            wrapper = ET.Element("SDGS")
            for item in self.sdgs:
                serialized = SerializationHelper.serialize_item(item, "Sdg")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "FileInfoComment":
        """Deserialize XML element to FileInfoComment object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized FileInfoComment object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(FileInfoComment, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "SDGS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.sdgs.append(SerializationHelper.deserialize_by_tag(item_elem, "Sdg"))

        return obj



class FileInfoCommentBuilder(BuilderBase):
    """Builder for FileInfoComment with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: FileInfoComment = FileInfoComment()


    def with_sdgs(self, items: list[Sdg]) -> "FileInfoCommentBuilder":
        """Set sdgs list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.sdgs = list(items) if items else []
        return self


    def add_sdg(self, item: Sdg) -> "FileInfoCommentBuilder":
        """Add a single item to sdgs list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.sdgs.append(item)
        return self

    def clear_sdgs(self) -> "FileInfoCommentBuilder":
        """Clear all items from sdgs list.

        Returns:
            self for method chaining
        """
        self._obj.sdgs = []
        return self


    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "sdg",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> FileInfoComment:
        """Build and return the FileInfoComment instance with validation."""
        self._validate_instance()
        return self._obj