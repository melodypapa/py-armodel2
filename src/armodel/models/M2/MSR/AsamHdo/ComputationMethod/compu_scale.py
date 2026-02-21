"""CompuScale AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 387)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2011)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 177)

JSON Source: docs/json/packages/M2_MSR_AsamHdo_ComputationMethod.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, get_type_hints
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.serialization.name_converter import NameConverter
from armodel.serialization.model_factory import ModelFactory

if TYPE_CHECKING:
    from typing import Self
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    CIdentifier,
    Identifier,
    Limit,
    PositiveUnlimitedInteger,
    String,
)
from armodel.models.M2.MSR.AsamHdo.ComputationMethod.compu_const import (
    CompuConst,
)
from armodel.models.M2.MSR.AsamHdo.ComputationMethod.compu_scale_contents import (
    CompuScaleContents,
)
from armodel.models.M2.MSR.Documentation.TextModel.MultilanguageData.multi_language_overview_paragraph import (
    MultiLanguageOverviewParagraph,
)


class CompuScale(ARObject):
    """AUTOSAR CompuScale."""

    # Polymorphic flattened mapping for compu_scale_contents attribute
    # Maps flattened child XML tags to wrapper class names
    _polymorphic_flattened_mapping = {
        "compu_scale_contents": {
            "COMPU-CONST": "CompuScaleConstantContents",
            "COMPU-RATIONAL-COEFFS": "CompuScaleRationalFormula"
        }
    }

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
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

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
            from armodel.models.M2.MSR.AsamHdo.ComputationMethod.compu_scale_constant_contents import CompuScaleConstantContents
            if isinstance(self.compu_scale_contents, CompuScaleConstantContents) and hasattr(self.compu_scale_contents, 'compu_const') and self.compu_scale_contents.compu_const is not None:
                # Add the COMPU-CONST directly (flattened structure)
                serialized = self.compu_scale_contents.compu_const.serialize()
                elem.append(serialized)

            # Handle CompuScaleRationalFormula flattening
            from armodel.models.M2.MSR.AsamHdo.ComputationMethod.compu_scale_rational_formula import CompuScaleRationalFormula
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
    def deserialize(cls, element: ET.Element) -> Self:
        """Deserialize XML element to CompuScale.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized CompuScale instance
        """
        # First, call parent's deserialize to handle inherited attributes (checksum, timestamp)
        obj = super(CompuScale, cls).deserialize(element)

        # Parse desc
        child = SerializationHelper.find_child_element(element, "DESC")
        if child is not None:
            # DESC contains L-2 children directly, wrap in MultiLanguageOverviewParagraph
            from armodel.models.M2.MSR.Documentation.TextModel.MultilanguageData.multi_language_overview_paragraph import MultiLanguageOverviewParagraph
            wrapped = MultiLanguageOverviewParagraph()
            for sub_child in child:
                sub_child_tag = SerializationHelper.strip_namespace(sub_child.tag)
                if sub_child_tag == "L-2":
                    l2_value = SerializationHelper.deserialize_by_tag(sub_child, "LParagraph")
                    if hasattr(wrapped, '_l2'):
                        wrapped._l2.append(l2_value)
            obj.desc = wrapped

        # Parse lower_limit
        child = SerializationHelper.find_child_element(element, "LOWER-LIMIT")
        if child is not None:
            obj.lower_limit = SerializationHelper.deserialize_by_tag(child, "Limit")

        # Parse upper_limit
        child = SerializationHelper.find_child_element(element, "UPPER-LIMIT")
        if child is not None:
            obj.upper_limit = SerializationHelper.deserialize_by_tag(child, "Limit")

        # Parse compu_scale_contents (flattened structure)
        # Check for COMPU-CONST
        child = SerializationHelper.find_child_element(element, "COMPU-CONST")
        if child is not None:
            from armodel.models.M2.MSR.AsamHdo.ComputationMethod.compu_scale_constant_contents import CompuScaleConstantContents
            from armodel.models.M2.MSR.AsamHdo.ComputationMethod.compu_const import CompuConst
            const_contents = CompuScaleConstantContents()
            const_contents.compu_const = SerializationHelper.unwrap_primitive(CompuConst.deserialize(child))
            obj.compu_scale_contents = const_contents

        # Check for COMPU-RATIONAL-COEFFS
        child = SerializationHelper.find_child_element(element, "COMPU-RATIONAL-COEFFS")
        if child is not None:
            from armodel.models.M2.MSR.AsamHdo.ComputationMethod.compu_scale_rational_formula import CompuScaleRationalFormula
            from armodel.models.M2.MSR.AsamHdo.ComputationMethod.compu_rational_coeffs import CompuRationalCoeffs
            rational_formula = CompuScaleRationalFormula()
            rational_formula.compu_rational_coeffs = SerializationHelper.unwrap_primitive(CompuRationalCoeffs.deserialize(child))
            obj.compu_scale_contents = rational_formula

        # Parse compu_inverse_value
        child = SerializationHelper.find_child_element(element, "COMPU-INVERSE-VALUE")
        if child is not None:
            obj.compu_inverse_value = SerializationHelper.unwrap_primitive(SerializationHelper.deserialize_by_tag(child, "CompuConst"))

        # Parse a2l_display_text
        child = SerializationHelper.find_child_element(element, "A2L-DISPLAY-TEXT")
        if child is not None:
            obj.a2l_display_text = SerializationHelper.deserialize_by_tag(child, "String")

        # Parse mask
        child = SerializationHelper.find_child_element(element, "MASK")
        if child is not None:
            obj.mask = SerializationHelper.deserialize_by_tag(child, "PositiveUnlimitedInteger")

        # Parse short_label
        child = SerializationHelper.find_child_element(element, "SHORT-LABEL")
        if child is not None:
            obj.short_label = SerializationHelper.deserialize_by_tag(child, "Identifier")

        # Parse symbol
        child = SerializationHelper.find_child_element(element, "SYMBOL")
        if child is not None:
            obj.symbol = SerializationHelper.deserialize_by_tag(child, "CIdentifier")

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
        # TODO: Add validation
        return self._obj
