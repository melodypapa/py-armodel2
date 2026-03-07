"""Note AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 310)

JSON Source: docs/json/packages/M2_MSR_Documentation_BlockElements_Note.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.MSR.Documentation.BlockElements.PaginationAndView.paginateable import (
    Paginateable,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.MSR.Documentation.BlockElements.PaginationAndView.paginateable import PaginateableBuilder
from armodel2.models.M2.MSR.Documentation.BlockElements.Note import (
    NoteTypeEnum,
)
from armodel2.models.M2.MSR.Documentation.TextModel.MultilanguageData.multilanguage_long_name import (
    MultilanguageLongName,
)

if TYPE_CHECKING:
    from armodel2.models.M2.MSR.Documentation.BlockElements.documentation_block import (
        DocumentationBlock,
    )



from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper
class Note(Paginateable):
    """AUTOSAR Note."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "NOTE"


    label: Optional[MultilanguageLongName]
    note_text: DocumentationBlock
    note_type: Optional[NoteTypeEnum]
    _DESERIALIZE_DISPATCH = {
        "LABEL": lambda obj, elem: setattr(obj, "label", SerializationHelper.deserialize_by_tag(elem, "MultilanguageLongName")),
        "NOTE-TEXT": lambda obj, elem: setattr(obj, "note_text", SerializationHelper.deserialize_by_tag(elem, "DocumentationBlock")),
        "NOTE-TYPE": lambda obj, elem: setattr(obj, "note_type", NoteTypeEnum.deserialize(elem)),
    }


    def __init__(self) -> None:
        """Initialize Note."""
        super().__init__()
        self.label: Optional[MultilanguageLongName] = None
        self.note_text: DocumentationBlock = None
        self.note_type: Optional[NoteTypeEnum] = None

    def serialize(self) -> ET.Element:
        """Serialize Note to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(Note, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize label
        if self.label is not None:
            serialized = SerializationHelper.serialize_item(self.label, "MultilanguageLongName")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("LABEL")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize note_text
        if self.note_text is not None:
            serialized = SerializationHelper.serialize_item(self.note_text, "DocumentationBlock")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("NOTE-TEXT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize note_type
        if self.note_type is not None:
            serialized = SerializationHelper.serialize_item(self.note_type, "NoteTypeEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("NOTE-TYPE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "Note":
        """Deserialize XML element to Note object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized Note object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(Note, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "LABEL":
                setattr(obj, "label", SerializationHelper.deserialize_by_tag(child, "MultilanguageLongName"))
            elif tag == "NOTE-TEXT":
                setattr(obj, "note_text", SerializationHelper.deserialize_by_tag(child, "DocumentationBlock"))
            elif tag == "NOTE-TYPE":
                setattr(obj, "note_type", NoteTypeEnum.deserialize(child))

        return obj



class NoteBuilder(PaginateableBuilder):
    """Builder for Note with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: Note = Note()


    def with_label(self, value: Optional[MultilanguageLongName]) -> "NoteBuilder":
        """Set label attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'label' is required and cannot be None")
        self._obj.label = value
        return self

    def with_note_text(self, value: DocumentationBlock) -> "NoteBuilder":
        """Set note_text attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not False:
            raise ValueError("Attribute 'note_text' is required and cannot be None")
        self._obj.note_text = value
        return self

    def with_note_type(self, value: Optional[NoteTypeEnum]) -> "NoteBuilder":
        """Set note_type attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'note_type' is required and cannot be None")
        self._obj.note_type = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _REQUIRED_ATTRIBUTES = {
        "noteText",
    }
    _OPTIONAL_ATTRIBUTES = {
        "label",
        "noteType",
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
        if getattr(self._obj, "noteText", None) is None:
            if mode == BuilderValidationMode.STRICT:
                raise ValueError("Required attribute 'noteText' is None")
            elif mode == BuilderValidationMode.LENIENT:
                import warnings
                warnings.warn("Required attribute 'noteText' is None", UserWarning)


    def build(self) -> Note:
        """Build and return the Note instance with validation."""
        self._validate_instance()
        return self._obj