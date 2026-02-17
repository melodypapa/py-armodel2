"""UserDefinedIPdu AUTOSAR element."""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject


class UserDefinedIPdu(IPdu):
    """AUTOSAR UserDefinedIPdu."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
    }

    def __init__(self) -> None:
        """Initialize UserDefinedIPdu."""
        super().__init__()


class UserDefinedIPduBuilder:
    """Builder for UserDefinedIPdu."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: UserDefinedIPdu = UserDefinedIPdu()

    def build(self) -> UserDefinedIPdu:
        """Build and return UserDefinedIPdu object.

        Returns:
            UserDefinedIPdu instance
        """
        # TODO: Add validation
        return self._obj
