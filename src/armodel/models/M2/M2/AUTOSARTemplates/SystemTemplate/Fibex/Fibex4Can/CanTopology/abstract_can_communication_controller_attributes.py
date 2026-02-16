"""AbstractCanCommunicationControllerAttributes AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject


class AbstractCanCommunicationControllerAttributes(ARObject):
    """AUTOSAR AbstractCanCommunicationControllerAttributes."""
    """Abstract base class - do not instantiate directly."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "can_controller_fd": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=any (CanControllerFd),
        ),  # canControllerFd
        "can_controller_xl": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=any (CanControllerXl),
        ),  # canControllerXl
    }

    def __init__(self) -> None:
        """Initialize AbstractCanCommunicationControllerAttributes."""
        super().__init__()
        self.can_controller_fd: Optional[Any] = None
        self.can_controller_xl: Optional[Any] = None


class AbstractCanCommunicationControllerAttributesBuilder:
    """Builder for AbstractCanCommunicationControllerAttributes."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: AbstractCanCommunicationControllerAttributes = AbstractCanCommunicationControllerAttributes()

    def build(self) -> AbstractCanCommunicationControllerAttributes:
        """Build and return AbstractCanCommunicationControllerAttributes object.

        Returns:
            AbstractCanCommunicationControllerAttributes instance
        """
        # TODO: Add validation
        return self._obj
