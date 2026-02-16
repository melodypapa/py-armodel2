"""EcucIndexableValue AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class EcucIndexableValue(ARObject):
    """AUTOSAR EcucIndexableValue."""
    """Abstract base class - do not instantiate directly."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "index": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # index
    }

    def __init__(self) -> None:
        """Initialize EcucIndexableValue."""
        super().__init__()
        self.index: Optional[PositiveInteger] = None


class EcucIndexableValueBuilder:
    """Builder for EcucIndexableValue."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EcucIndexableValue = EcucIndexableValue()

    def build(self) -> EcucIndexableValue:
        """Build and return EcucIndexableValue object.

        Returns:
            EcucIndexableValue instance
        """
        # TODO: Add validation
        return self._obj
