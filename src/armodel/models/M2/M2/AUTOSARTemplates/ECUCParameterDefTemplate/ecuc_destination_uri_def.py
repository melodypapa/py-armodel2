"""EcucDestinationUriDef AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)


class EcucDestinationUriDef(Identifiable):
    """AUTOSAR EcucDestinationUriDef."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "destination_uri": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=any (EcucDestinationUri),
        ),  # destinationUri
    }

    def __init__(self) -> None:
        """Initialize EcucDestinationUriDef."""
        super().__init__()
        self.destination_uri: Optional[Any] = None


class EcucDestinationUriDefBuilder:
    """Builder for EcucDestinationUriDef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EcucDestinationUriDef = EcucDestinationUriDef()

    def build(self) -> EcucDestinationUriDef:
        """Build and return EcucDestinationUriDef object.

        Returns:
            EcucDestinationUriDef instance
        """
        # TODO: Add validation
        return self._obj
