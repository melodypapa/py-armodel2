"""SingleLanguageReferrable AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 64)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_GenericStructure_GeneralTemplateClasses_Identifiable.classes.json"""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.referrable import (
    Referrable,
)
from armodel.models.M2.MSR.Documentation.TextModel.SingleLanguageData.single_language_long_name import (
    SingleLanguageLongName,
)


class SingleLanguageReferrable(Referrable):
    """AUTOSAR SingleLanguageReferrable."""
    """Abstract base class - do not instantiate directly."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "long_name1": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=SingleLanguageLongName,
        ),  # longName1
    }

    def __init__(self) -> None:
        """Initialize SingleLanguageReferrable."""
        super().__init__()
        self.long_name1: Optional[SingleLanguageLongName] = None


class SingleLanguageReferrableBuilder:
    """Builder for SingleLanguageReferrable."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SingleLanguageReferrable = SingleLanguageReferrable()

    def build(self) -> SingleLanguageReferrable:
        """Build and return SingleLanguageReferrable object.

        Returns:
            SingleLanguageReferrable instance
        """
        # TODO: Add validation
        return self._obj
