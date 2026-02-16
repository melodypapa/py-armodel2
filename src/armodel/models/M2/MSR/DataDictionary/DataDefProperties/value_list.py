"""ValueList AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Numerical,
)


class ValueList(ARObject):
    """AUTOSAR ValueList."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "v": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # v
    }

    def __init__(self) -> None:
        """Initialize ValueList."""
        super().__init__()
        self.v: Optional[Numerical] = None


class ValueListBuilder:
    """Builder for ValueList."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ValueList = ValueList()

    def build(self) -> ValueList:
        """Build and return ValueList object.

        Returns:
            ValueList instance
        """
        # TODO: Add validation
        return self._obj
