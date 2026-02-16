"""AccessCount AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.AccessCount.abstract_access_point import (
    AbstractAccessPoint,
)


class AccessCount(ARObject):
    """AUTOSAR AccessCount."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "access_point": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=AbstractAccessPoint,
        ),  # accessPoint
        "value": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # value
    }

    def __init__(self) -> None:
        """Initialize AccessCount."""
        super().__init__()
        self.access_point: Optional[AbstractAccessPoint] = None
        self.value: Optional[PositiveInteger] = None


class AccessCountBuilder:
    """Builder for AccessCount."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: AccessCount = AccessCount()

    def build(self) -> AccessCount:
        """Build and return AccessCount object.

        Returns:
            AccessCount instance
        """
        # TODO: Add validation
        return self._obj
