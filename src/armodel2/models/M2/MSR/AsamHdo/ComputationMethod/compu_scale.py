"""CompuScale AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 387)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2011)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 177)

JSON Source: docs/json/packages/M2_MSR_AsamHdo_ComputationMethod.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, get_type_hints
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper
from armodel2.serialization.name_converter import NameConverter
from armodel2.serialization.model_factory import ModelFactory

if TYPE_CHECKING:
    from typing import Self
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    CIdentifier,
    Identifier,
    Limit,
    PositiveUnlimitedInteger,
    String,
)
from armodel2.models.M2.MSR.AsamHdo.ComputationMethod.compu_const import (
    CompuConst,
)
from armodel2.models.M2.MSR.AsamHdo.ComputationMethod.compu_scale_contents import (
    CompuScaleContents,
)
from armodel2.models.M2.MSR.Documentation.TextModel.MultilanguageData.multi_language_overview_paragraph import (
    MultiLanguageOverviewParagraph,
)


class CompuScale(ARObject):
    """AUTOSAR CompuScale."""

    _XML_TAG = "COMPU-SCALE"

    # Polymorphic flattened mapping for compu_scale_contents attribute
    # Maps flattened child XML tags to wrapper class names
    _polymorphic_flattened_mapping = {
        "compu_scale_contents": {
            "COMPU-CONST": "CompuScaleConstantContents",
            "COMPU-RATIONAL-COEFFS": "CompuScaleRationalFormula"
        }
    }

    _DESERIALIZE_DISPATCH = {
        "DESC": lambda obj, elem: setattr(obj, 'desc', CompuScale._deserialize_desc(elem)),
        "LOWER-LIMIT": lambda obj, elem: setattr(obj, 'lower_limit', SerializationHelper.deserialize_by_tag(elem, "Limit")),
        "UPPER-LIMIT": lambda obj, elem: setattr(obj, 'upper_limit', SerializationHelper.deserialize_by_tag(elem, "Limit")),
        "COMPU-CONST": lambda obj, elem: CompuScale._deserialize_compu_const(obj, elem),
        "COMPU-RATIONAL-COEFFS": lambda obj, elem: CompuScale._deserialize_compu_rational(obj, elem),
        "COMPU-INVERSE-VALUE": lambda obj, elem: setattr(obj, 'compu_inverse_value', SerializationHelper.unwrap_primitive(SerializationHelper.deserialize_by_tag(elem, "CompuConst"))),
        "A2L-DISPLAY-TEXT": lambda obj, elem: setattr(obj, 'a2l_display_text', SerializationHelper.deserialize_by_tag(elem, "String")),
        "MASK": lambda obj, elem: setattr(obj, 'mask', SerializationHelper.deserialize_by_tag(elem, "PositiveUnlimitedInteger")),
        "SHORT-LABEL": lambda obj, elem: setattr(obj, 'short_label', SerializationHelper.deserialize_by_tag(elem, "Identifier")),
        "SYMBOL": lambda obj, elem: setattr(obj, 'symbol', SerializationHelper.deserialize_by_tag(elem, "CIdentifier")),
    }

    @staticmethod
    def _deserialize_desc(elem: ET.Element) -> Optional[MultiLanguageOverviewParagraph]:
        """Deserialize DESC element with L-2 children."""
        from armodel2.models.M2.MSR.Documentation.TextModel.MultilanguageData.multi_language_overview_paragraph import MultiLanguageOverviewParagraph
        from armodel2.models.M2.MSR.Documentation.TextModel.LanguageDataModel.l_paragraph import LParagraph

        wrapped = MultiLanguageOverviewParagraph()
        for sub_child in elem:
            sub_child_tag = SerializationHelper.strip_namespace(sub_child.tag)
            if sub_child_tag == "L-2":
                l2_value = SerializationHelper.deserialize_by_tag(sub_child, "LParagraph")
                if hasattr(wrapped, '_l2'):
                    wrapped._l2.append(l2_value)
        return wrapped if len(wrapped._l2) > 0 else None

    @staticmethod
    def _deserialize_compu_const(obj: "CompuScale", elem: ET.Element) -> None:
        """Deserialize COMPU-CONST for compu_scale_contents."""
        from armodel2.models.M2.MSR.AsamHdo.ComputationMethod.compu_scale_constant_contents import CompuScaleConstantContents
        const_contents = CompuScaleConstantContents()
        const_contents.compu_const = SerializationHelper.unwrap_primitive(CompuConst.deserialize(elem))
        obj.compu_scale_contents = const_contents

    @staticmethod
    def _deserialize_compu_rational(obj: "CompuScale", elem: ET.Element) -> None:
        """Deserialize COMPU-RATIONAL-COEFFS for compu_scale_contents."""
        from armodel2.models.M2.MSR.AsamHdo.ComputationMethod.compu_scale_rational_formula import CompuScaleRationalFormula
        from armodel2.models.M2.MSR.AsamHdo.ComputationMethod.compu_rational_coeffs import CompuRationalCoeffs
        rational_formula = CompuScaleRationalFormula()
        rational_formula.compu_rational_coeffs = SerializationHelper.unwrap_primitive(CompuRationalCoeffs.deserialize(elem))
        obj.compu_scale_contents = rational_formula

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    a2l_display_text: Optional[String]
    compu_inverse_value: Optional[CompuConst]
    compu_scale_contents: Optional[CompuScaleContents]
    desc: Optional[MultiLanguageOverviewParagraph]
    lower_limit: Optional[Limit]
    mask: Optional[PositiveUnlimitedInteger]
    short_label: Optional[Identifier]
    symbol: Optional[CIdentifier]
    upper_limit: Optional[Limit]
    def __init__(self) -> None:
        """Initialize CompuScale."""
        super().__init__()
        self.a2l_display_text: Optional[String] = None
        self.compu_inverse_value: Optional[CompuConst] = None
        self.compu_scale_contents: Optional[CompuScaleContents] = None
        self.desc: Optional[MultiLanguageOverviewParagraph] = None
        self.lower_limit: Optional[Limit] = None
        self.mask: Optional[PositiveUnlimitedInteger] = None
        self.short_label: Optional[Identifier] = None
        self.symbol: Optional[CIdentifier] = None
        self.upper_limit: Optional[Limit] = None

    def serialize(self) -> ET.Element:
        """Serialize CompuScale to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this CompuScale
        """
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes (checksum, timestamp)
        parent_elem = super(CompuScale, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize desc
        if self.desc is not None:
            serialized = self.desc.serialize()
            # The DESC element should contain L-2 children directly, not MULTI-LANGUAGE-OVERVIEW-PARAGRAPH
            # So we unwrap the wrapper
            wrapped = ET.Element("DESC")
            if hasattr(serialized, 'attrib'):
                wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
            for child in serialized:
                wrapped.append(child)
            elem.append(wrapped)

        # Serialize lower_limit
        if self.lower_limit is not None:
            serialized = SerializationHelper.serialize_item(self.lower_limit, "Limit")
            if serialized is not None:
                wrapped = ET.Element("LOWER-LIMIT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize upper_limit
        if self.upper_limit is not None:
            serialized = SerializationHelper.serialize_item(self.upper_limit, "Limit")
            if serialized is not None:
                wrapped = ET.Element("UPPER-LIMIT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Handle compu_scale_contents specially for flattened structure
        if self.compu_scale_contents is not None:
            # Handle CompuScaleConstantContents flattening
            from armodel2.models.M2.MSR.AsamHdo.ComputationMethod.compu_scale_constant_contents import CompuScaleConstantContents
            if isinstance(self.compu_scale_contents, CompuScaleConstantContents) and hasattr(self.compu_scale_contents, 'compu_const') and self.compu_scale_contents.compu_const is not None:
                # Add the COMPU-CONST directly (flattened structure)
                serialized = self.compu_scale_contents.compu_const.serialize()
                elem.append(serialized)

            # Handle CompuScaleRationalFormula flattening
            from armodel2.models.M2.MSR.AsamHdo.ComputationMethod.compu_scale_rational_formula import CompuScaleRationalFormula
            if isinstance(self.compu_scale_contents, CompuScaleRationalFormula) and hasattr(self.compu_scale_contents, 'compu_rational_coeffs') and self.compu_scale_contents.compu_rational_coeffs is not None:
                # Add the COMPU-RATIONAL-COEFFS directly (flattened structure)
                serialized = self.compu_scale_contents.compu_rational_coeffs.serialize()
                # Wrap with COMPU-RATIONAL-COEFFS tag
                wrapped = ET.Element("COMPU-RATIONAL-COEFFS")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize compu_inverse_value
        if self.compu_inverse_value is not None:
            serialized = SerializationHelper.serialize_item(self.compu_inverse_value, "CompuConst")
            if serialized is not None:
                wrapped = ET.Element("COMPU-INVERSE-VALUE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize a2l_display_text
        if self.a2l_display_text is not None:
            serialized = SerializationHelper.serialize_item(self.a2l_display_text, "String")
            if serialized is not None:
                wrapped = ET.Element("A2L-DISPLAY-TEXT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize mask
        if self.mask is not None:
            serialized = SerializationHelper.serialize_item(self.mask, "PositiveUnlimitedInteger")
            if serialized is not None:
                wrapped = ET.Element("MASK")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize short_label
        if self.short_label is not None:
            serialized = SerializationHelper.serialize_item(self.short_label, "Identifier")
            if serialized is not None:
                wrapped = ET.Element("SHORT-LABEL")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize symbol
        if self.symbol is not None:
            serialized = SerializationHelper.serialize_item(self.symbol, "CIdentifier")
            if serialized is not None:
                wrapped = ET.Element("SYMBOL")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Reorder elements to match AUTOSAR XML schema order
        # The correct order is: DESC, LOWER-LIMIT, UPPER-LIMIT, COMPU-CONST/COMPU-RATIONAL-COEFFS, ...
        # Extract all children and reorder them
        children = list(elem)
        elem.clear()  # Remove all children

        # Define the desired order of elements
        element_order = [
            "DESC",
            "LOWER-LIMIT",
            "UPPER-LIMIT",
            "COMPU-CONST",
            "COMPU-RATIONAL-COEFFS",
            "COMPU-INVERSE-VALUE",
            "A2L-DISPLAY-TEXT",
            "MASK",
            "SHORT-LABEL",
            "SYMBOL",
        ]

        # Add elements in the desired order
        for tag in element_order:
            for child in children:
                child_tag = SerializationHelper.strip_namespace(child.tag)
                if child_tag == tag:
                    elem.append(child)
                    break

        # Add any remaining elements that weren't in the ordered list
        for child in children:
            child_tag = SerializationHelper.strip_namespace(child.tag)
            if child_tag not in element_order:
                elem.append(child)
        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "CompuScale":
        """Deserialize XML element to CompuScale.

        Uses static dispatch table for O(1) tag-to-handler lookup.
        Calls super().deserialize() first to handle inherited attributes from ARObject.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized CompuScale instance
        """
        # First, deserialize inherited attributes from parent chain (ARObject)
        obj = super(CompuScale, cls).deserialize(element)

        # Then process CompuScale-specific elements with dispatch table
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            handler = cls._DESERIALIZE_DISPATCH.get(tag)
            if handler is not None:
                handler(obj, child)

        return obj


class CompuScaleBuilder:
    """Builder for CompuScale."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CompuScale = CompuScale()

    def build(self) -> CompuScale:
        """Build and return CompuScale object.

        Returns:
            CompuScale instance
        """
        return self._obj
