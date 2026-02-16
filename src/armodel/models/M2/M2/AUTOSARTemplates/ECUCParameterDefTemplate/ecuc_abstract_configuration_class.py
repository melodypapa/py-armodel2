"""EcucAbstractConfigurationClass AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject


class EcucAbstractConfigurationClass(ARObject):
    """AUTOSAR EcucAbstractConfigurationClass."""
    """Abstract base class - do not instantiate directly."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "config_class": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=EcucConfigurationClassEnum,
        ),  # configClass
        "config_variant": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=any (EcucConfiguration),
        ),  # configVariant
    }

    def __init__(self) -> None:
        """Initialize EcucAbstractConfigurationClass."""
        super().__init__()
        self.config_class: Optional[EcucConfigurationClassEnum] = None
        self.config_variant: Optional[Any] = None


class EcucAbstractConfigurationClassBuilder:
    """Builder for EcucAbstractConfigurationClass."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EcucAbstractConfigurationClass = EcucAbstractConfigurationClass()

    def build(self) -> EcucAbstractConfigurationClass:
        """Build and return EcucAbstractConfigurationClass object.

        Returns:
            EcucAbstractConfigurationClass instance
        """
        # TODO: Add validation
        return self._obj
