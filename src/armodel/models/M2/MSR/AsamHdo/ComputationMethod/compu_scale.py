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

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    a2l_display_text: Optional[String]
    compu_inverse: Optional[CompuConst]
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
        self.compu_inverse: Optional[CompuConst] = None
        self.compu_scale_contents: Optional[CompuScaleContents] = None
        self.desc: Optional[MultiLanguageOverviewParagraph] = None
        self.lower_limit: Optional[Limit] = None
        self.mask: Optional[PositiveUnlimitedInteger] = None
        self.short_label: Optional[Identifier] = None
        self.symbol: Optional[CIdentifier] = None
        self.upper_limit: Optional[Limit] = None

    def serialize(self) -> ET.Element:
        """Serialize CompuScale to XML element.

        Handles flattened COMPU-CONST structure where COMPU-CONST can appear
        directly under COMPU-SCALE instead of being wrapped in COMPU-SCALE-CONSTANT-CONTENTS.

        Returns:
            xml.etree.ElementTree.Element representing this CompuScale
        """
        # First, call parent class serialize to get standard serialization
        elem = super().serialize()

        # Now handle compu_scale_contents specially for flattened structure
        # Check if we have COMPU-SCALE-CONSTANT-CONTENTS that needs to be flattened
        if self.compu_scale_contents is not None:
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

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> Self:
        """Deserialize XML element to CompuScale.

        Handles flattened COMPU-CONST structure where COMPU-CONST can appear
        directly under COMPU-SCALE instead of being wrapped in COMPU-SCALE-CONSTANT-CONTENTS.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized CompuScale instance
        """
        # First, use the parent class deserialize to handle standard attributes
        obj = super().deserialize(element)

        # Now check for COMPU-CONST elements that weren't handled by standard deserialization
        # (they would have been ignored as unrecognized elements)
        compu_const_elements = []
        for child in element:
            child_tag = ARObject._strip_namespace(child.tag)
            if child_tag == "COMPU-CONST":
                compu_const_elements.append(child)

        # Handle COMPU-CONST elements (flattened structure)
        if compu_const_elements and obj.compu_scale_contents is None:
            from armodel.models.M2.MSR.AsamHdo.ComputationMethod.compu_scale_constant_contents import CompuScaleConstantContents
            from armodel.models.M2.MSR.AsamHdo.ComputationMethod.compu_const import CompuConst

            # Create CompuScaleConstantContents wrapper
            constant_contents = CompuScaleConstantContents()

            # Deserialize the first COMPU-CONST
            compu_const = CompuConst.deserialize(compu_const_elements[0])
            constant_contents.compu_const = compu_const

            # Set as compu_scale_contents
            obj.compu_scale_contents = constant_contents

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
