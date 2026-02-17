"""NumericalOrText AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 323)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 455)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Constants.classes.json"""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Numerical,
    String,
)


class NumericalOrText(ARObject):
    """AUTOSAR NumericalOrText."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "vf": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # vf
        "vt": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # vt
    }

    def __init__(self) -> None:
        """Initialize NumericalOrText."""
        super().__init__()
        self.vf: Optional[Numerical] = None
        self.vt: Optional[String] = None


class NumericalOrTextBuilder:
    """Builder for NumericalOrText."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: NumericalOrText = NumericalOrText()

    def build(self) -> NumericalOrText:
        """Build and return NumericalOrText object.

        Returns:
            NumericalOrText instance
        """
        # TODO: Add validation
        return self._obj
