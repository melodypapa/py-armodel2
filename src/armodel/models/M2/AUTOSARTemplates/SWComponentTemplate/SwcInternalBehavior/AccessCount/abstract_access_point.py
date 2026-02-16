"""AbstractAccessPoint AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)


class AbstractAccessPoint(Identifiable):
    """AUTOSAR AbstractAccessPoint."""
    """Abstract base class - do not instantiate directly."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "return_value": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=RteApiReturnValueProvisionEnum,
        ),  # returnValue
    }

    def __init__(self) -> None:
        """Initialize AbstractAccessPoint."""
        super().__init__()
        self.return_value: Optional[RteApiReturnValueProvisionEnum] = None


class AbstractAccessPointBuilder:
    """Builder for AbstractAccessPoint."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: AbstractAccessPoint = AbstractAccessPoint()

    def build(self) -> AbstractAccessPoint:
        """Build and return AbstractAccessPoint object.

        Returns:
            AbstractAccessPoint instance
        """
        # TODO: Add validation
        return self._obj
