"""CompuScaleConstantContents AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 390)

JSON Source: docs/json/packages/M2_MSR_AsamHdo_ComputationMethod.classes.json"""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.MSR.AsamHdo.ComputationMethod.compu_scale_contents import (
    CompuScaleContents,
)
from armodel.models.M2.MSR.AsamHdo.ComputationMethod.compu_const import (
    CompuConst,
)


class CompuScaleConstantContents(CompuScaleContents):
    """AUTOSAR CompuScaleConstantContents."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "compu_const": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=CompuConst,
        ),  # compuConst
    }

    def __init__(self) -> None:
        """Initialize CompuScaleConstantContents."""
        super().__init__()
        self.compu_const: Optional[CompuConst] = None


class CompuScaleConstantContentsBuilder:
    """Builder for CompuScaleConstantContents."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CompuScaleConstantContents = CompuScaleConstantContents()

    def build(self) -> CompuScaleConstantContents:
        """Build and return CompuScaleConstantContents object.

        Returns:
            CompuScaleConstantContents instance
        """
        # TODO: Add validation
        return self._obj
