"""IndentSample AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 297)

JSON Source: docs/json/packages/M2_MSR_Documentation_BlockElements_ListElements.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.MSR.Documentation.BlockElements.ListElements import (
    ItemLabelPosEnum,
)
from armodel2.models.M2.MSR.Documentation.TextModel.LanguageDataModel.l_overview_paragraph import (
    LOverviewParagraph,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class IndentSample(ARObject):
    """AUTOSAR IndentSample."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "INDENT-SAMPLE"


    item_label_pos_enum: Optional[ItemLabelPosEnum]
    l2: LOverviewParagraph
    _DESERIALIZE_DISPATCH = {
        "ITEM-LABEL-POS-ENUM": lambda obj, elem: setattr(obj, "item_label_pos_enum", ItemLabelPosEnum.deserialize(elem)),
        "L2": lambda obj, elem: setattr(obj, "l2", SerializationHelper.deserialize_by_tag(elem, "LOverviewParagraph")),
    }


    def __init__(self) -> None:
        """Initialize IndentSample."""
        super().__init__()
        self.item_label_pos_enum: Optional[ItemLabelPosEnum] = None
        self.l2: LOverviewParagraph = None

    def serialize(self) -> ET.Element:
        """Serialize IndentSample to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(IndentSample, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize item_label_pos_enum
        if self.item_label_pos_enum is not None:
            serialized = SerializationHelper.serialize_item(self.item_label_pos_enum, "ItemLabelPosEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ITEM-LABEL-POS-ENUM")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize l2
        if self.l2 is not None:
            serialized = SerializationHelper.serialize_item(self.l2, "LOverviewParagraph")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("L2")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "IndentSample":
        """Deserialize XML element to IndentSample object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized IndentSample object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(IndentSample, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "ITEM-LABEL-POS-ENUM":
                setattr(obj, "item_label_pos_enum", ItemLabelPosEnum.deserialize(child))
            elif tag == "L2":
                setattr(obj, "l2", SerializationHelper.deserialize_by_tag(child, "LOverviewParagraph"))

        return obj



class IndentSampleBuilder(BuilderBase):
    """Builder for IndentSample with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: IndentSample = IndentSample()


    def with_item_label_pos_enum(self, value: Optional[ItemLabelPosEnum]) -> "IndentSampleBuilder":
        """Set item_label_pos_enum attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'item_label_pos_enum' is required and cannot be None")
        self._obj.item_label_pos_enum = value
        return self

    def with_l2(self, value: LOverviewParagraph) -> "IndentSampleBuilder":
        """Set l2 attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not False:
            raise ValueError("Attribute 'l2' is required and cannot be None")
        self._obj.l2 = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _REQUIRED_ATTRIBUTES = {
        "l2",
    }
    _OPTIONAL_ATTRIBUTES = {
        "itemLabelPosEnum",
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
        if getattr(self._obj, "l2", None) is None:
            if mode == BuilderValidationMode.STRICT:
                raise ValueError("Required attribute 'l2' is None")
            elif mode == BuilderValidationMode.LENIENT:
                import warnings
                warnings.warn("Required attribute 'l2' is None", UserWarning)


    def build(self) -> IndentSample:
        """Build and return the IndentSample instance with validation."""
        self._validate_instance()
        return self._obj