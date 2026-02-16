"""SwcExclusiveAreaPolicy AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.CommonStructure.InternalBehavior.exclusive_area import (
    ExclusiveArea,
)


class SwcExclusiveAreaPolicy(ARObject):
    """AUTOSAR SwcExclusiveAreaPolicy."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "api_principle_enum": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=ApiPrincipleEnum,
        ),  # apiPrincipleEnum
        "exclusive_area": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=ExclusiveArea,
        ),  # exclusiveArea
    }

    def __init__(self) -> None:
        """Initialize SwcExclusiveAreaPolicy."""
        super().__init__()
        self.api_principle_enum: Optional[ApiPrincipleEnum] = None
        self.exclusive_area: Optional[ExclusiveArea] = None


class SwcExclusiveAreaPolicyBuilder:
    """Builder for SwcExclusiveAreaPolicy."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SwcExclusiveAreaPolicy = SwcExclusiveAreaPolicy()

    def build(self) -> SwcExclusiveAreaPolicy:
        """Build and return SwcExclusiveAreaPolicy object.

        Returns:
            SwcExclusiveAreaPolicy instance
        """
        # TODO: Add validation
        return self._obj
