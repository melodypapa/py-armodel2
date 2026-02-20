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
from armodel.serialization.name_converter import NameConverter
from armodel.serialization.model_factory import ModelFactory
from armodel.serialization.decorators import polymorphic_flattened

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
        # First, call parent class serialize to get standard serialization
        elem = super().serialize()

        # Handle desc attribute - unwrap MultiLanguageOverviewParagraph wrapper
        # The DESC element should contain L-2 children directly, not MULTI-LANGUAGE-OVERVIEW-PARAGRAPH
        for child in list(elem):
            child_tag = ARObject._strip_namespace(child.tag)
            if child_tag == "MULTI-LANGUAGE-OVERVIEW-PARAGRAPH":
                elem.remove(child)
                # Wrap with DESC tag and copy children
                wrapped = ET.Element("DESC")
                if hasattr(child, 'attrib'):
                    wrapped.attrib.update(child.attrib)
                    if child.text:
                        wrapped.text = child.text
                for sub_child in child:
                    wrapped.append(sub_child)
                elem.append(wrapped)
                break

        # Now handle compu_scale_contents specially for flattened structure
        if self.compu_scale_contents is not None:
            # Handle CompuScaleConstantContents flattening
            from armodel.models.M2.MSR.AsamHdo.ComputationMethod.compu_scale_constant_contents import CompuScaleConstantContents
            if isinstance(self.compu_scale_contents, CompuScaleConstantContents) and hasattr(self.compu_scale_contents, 'compu_const') and self.compu_scale_contents.compu_const is not None:
                # Remove the COMPU-SCALE-CONSTANT-CONTENTS wrapper if it exists
                for child in list(elem):
                    child_tag = ARObject._strip_namespace(child.tag)
                    if child_tag == "COMPU-SCALE-CONSTANT-CONTENTS":
                        elem.remove(child)
                        # Add the COMPU-CONST directly (flattened structure)
                        serialized = self.compu_scale_contents.compu_const.serialize()
                        elem.append(serialized)
                        break

            # Handle CompuScaleRationalFormula flattening
            from armodel.models.M2.MSR.AsamHdo.ComputationMethod.compu_scale_rational_formula import CompuScaleRationalFormula
            if isinstance(self.compu_scale_contents, CompuScaleRationalFormula) and hasattr(self.compu_scale_contents, 'compu_rational_coeffs') and self.compu_scale_contents.compu_rational_coeffs is not None:
                # Remove the COMPU-SCALE-RATIONAL-FORMULA wrapper if it exists
                for child in list(elem):
                    child_tag = ARObject._strip_namespace(child.tag)
                    if child_tag == "COMPU-SCALE-RATIONAL-FORMULA":
                        elem.remove(child)
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
                        break

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
        ]

        # Add elements in the desired order
        for tag in element_order:
            for child in children:
                child_tag = ARObject._strip_namespace(child.tag)
                if child_tag == tag:
                    elem.append(child)
                    break

        # Add any remaining elements that weren't in the ordered list
        for child in children:
            child_tag = ARObject._strip_namespace(child.tag)
            if child_tag not in element_order:
                elem.append(child)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> Self:
        """Deserialize XML element to CompuScale.

        The @polymorphic_flattened decorator on compu_scale_contents handles
        flattened COMPU-CONST and COMPU-RATIONAL-COEFFS elements that can appear
        directly under COMPU-SCALE without their wrapper elements.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized CompuScale instance
        """
        # Delegate to parent class deserialize - the @polymorphic_flattened
        # decorator in ARObject.deserialize() will handle flattened child elements
        return super().deserialize(element)


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
