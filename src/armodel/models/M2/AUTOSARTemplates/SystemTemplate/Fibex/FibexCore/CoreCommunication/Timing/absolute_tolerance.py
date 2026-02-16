"""AbsoluteTolerance AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    TimeValue,
)


class AbsoluteTolerance(ARObject):
    """AUTOSAR AbsoluteTolerance."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "absolute": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # absolute
    }

    def __init__(self) -> None:
        """Initialize AbsoluteTolerance."""
        super().__init__()
        self.absolute: Optional[TimeValue] = None


class AbsoluteToleranceBuilder:
    """Builder for AbsoluteTolerance."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: AbsoluteTolerance = AbsoluteTolerance()

    def build(self) -> AbsoluteTolerance:
        """Build and return AbsoluteTolerance object.

        Returns:
            AbsoluteTolerance instance
        """
        # TODO: Add validation
        return self._obj
