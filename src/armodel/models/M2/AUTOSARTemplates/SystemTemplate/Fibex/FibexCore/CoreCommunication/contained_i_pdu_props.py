"""ContainedIPduProps AUTOSAR element."""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject


class ContainedIPduProps(ARObject):
    """AUTOSAR ContainedIPduProps."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
    }

    def __init__(self) -> None:
        """Initialize ContainedIPduProps."""
        super().__init__()


class ContainedIPduPropsBuilder:
    """Builder for ContainedIPduProps."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ContainedIPduProps = ContainedIPduProps()

    def build(self) -> ContainedIPduProps:
        """Build and return ContainedIPduProps object.

        Returns:
            ContainedIPduProps instance
        """
        # TODO: Add validation
        return self._obj
