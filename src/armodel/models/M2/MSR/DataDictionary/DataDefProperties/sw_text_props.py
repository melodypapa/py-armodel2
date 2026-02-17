"""SwTextProps AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 343)
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 313)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 249)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 216)

JSON Source: docs/json/packages/M2_MSR_DataDictionary_DataDefProperties.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ImplementationDataTypes import (
    ArraySizeSemanticsEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Integer,
)
from armodel.models.M2.MSR.AsamHdo.BaseTypes.sw_base_type import (
    SwBaseType,
)


class SwTextProps(ARObject):
    """AUTOSAR SwTextProps."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "array_size": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=ArraySizeSemanticsEnum,
        ),  # arraySize
        "base_type": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=SwBaseType,
        ),  # baseType
        "sw_fill_character": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # swFillCharacter
        "sw_max_text_size": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # swMaxTextSize
    }

    def __init__(self) -> None:
        """Initialize SwTextProps."""
        super().__init__()
        self.array_size: Optional[ArraySizeSemanticsEnum] = None
        self.base_type: Optional[SwBaseType] = None
        self.sw_fill_character: Optional[Integer] = None
        self.sw_max_text_size: Optional[Integer] = None


class SwTextPropsBuilder:
    """Builder for SwTextProps."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SwTextProps = SwTextProps()

    def build(self) -> SwTextProps:
        """Build and return SwTextProps object.

        Returns:
            SwTextProps instance
        """
        # TODO: Add validation
        return self._obj
