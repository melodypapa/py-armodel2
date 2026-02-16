"""RunnableEntityArgument AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    CIdentifier,
)


class RunnableEntityArgument(ARObject):
    """AUTOSAR RunnableEntityArgument."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "symbol": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # symbol
    }

    def __init__(self) -> None:
        """Initialize RunnableEntityArgument."""
        super().__init__()
        self.symbol: Optional[CIdentifier] = None


class RunnableEntityArgumentBuilder:
    """Builder for RunnableEntityArgument."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: RunnableEntityArgument = RunnableEntityArgument()

    def build(self) -> RunnableEntityArgument:
        """Build and return RunnableEntityArgument object.

        Returns:
            RunnableEntityArgument instance
        """
        # TODO: Add validation
        return self._obj
