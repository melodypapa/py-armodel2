"""UserDefinedTransformationISignalProps AUTOSAR element."""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject


class UserDefinedTransformationISignalProps(ARObject):
    """AUTOSAR UserDefinedTransformationISignalProps."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
    }

    def __init__(self) -> None:
        """Initialize UserDefinedTransformationISignalProps."""
        super().__init__()


class UserDefinedTransformationISignalPropsBuilder:
    """Builder for UserDefinedTransformationISignalProps."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: UserDefinedTransformationISignalProps = UserDefinedTransformationISignalProps()

    def build(self) -> UserDefinedTransformationISignalProps:
        """Build and return UserDefinedTransformationISignalProps object.

        Returns:
            UserDefinedTransformationISignalProps instance
        """
        # TODO: Add validation
        return self._obj
