"""SOMEIPTransformationProps AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 783)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Transformer.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Transformer.transformation_props import (
    TransformationProps,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class SOMEIPTransformationProps(TransformationProps):
    """AUTOSAR SOMEIPTransformationProps."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "alignment": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # alignment
        "size_of_array": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # sizeOfArray
        "size_of_string": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # sizeOfString
        "size_of_struct": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # sizeOfStruct
        "size_of_union": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # sizeOfUnion
    }

    def __init__(self) -> None:
        """Initialize SOMEIPTransformationProps."""
        super().__init__()
        self.alignment: Optional[PositiveInteger] = None
        self.size_of_array: Optional[PositiveInteger] = None
        self.size_of_string: Optional[PositiveInteger] = None
        self.size_of_struct: Optional[PositiveInteger] = None
        self.size_of_union: Optional[PositiveInteger] = None


class SOMEIPTransformationPropsBuilder:
    """Builder for SOMEIPTransformationProps."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SOMEIPTransformationProps = SOMEIPTransformationProps()

    def build(self) -> SOMEIPTransformationProps:
        """Build and return SOMEIPTransformationProps object.

        Returns:
            SOMEIPTransformationProps instance
        """
        # TODO: Add validation
        return self._obj
