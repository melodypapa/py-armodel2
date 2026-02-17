"""HwAttributeValue AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_ECUResourceTemplate.pdf (page 16)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_EcuResourceTemplate_HwElementCategory.classes.json"""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Numerical,
    VerbatimString,
)
from armodel.models.M2.MSR.Documentation.Annotation.annotation import (
    Annotation,
)
from armodel.models.M2.AUTOSARTemplates.EcuResourceTemplate.HwElementCategory.hw_attribute_def import (
    HwAttributeDef,
)


class HwAttributeValue(ARObject):
    """AUTOSAR HwAttributeValue."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "annotation": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=Annotation,
        ),  # annotation
        "hw_attribute_def": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=HwAttributeDef,
        ),  # hwAttributeDef
        "v": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # v
        "vt": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # vt
    }

    def __init__(self) -> None:
        """Initialize HwAttributeValue."""
        super().__init__()
        self.annotation: Optional[Annotation] = None
        self.hw_attribute_def: Optional[HwAttributeDef] = None
        self.v: Optional[Numerical] = None
        self.vt: Optional[VerbatimString] = None


class HwAttributeValueBuilder:
    """Builder for HwAttributeValue."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: HwAttributeValue = HwAttributeValue()

    def build(self) -> HwAttributeValue:
        """Build and return HwAttributeValue object.

        Returns:
            HwAttributeValue instance
        """
        # TODO: Add validation
        return self._obj
