"""LinErrorResponse AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.i_signal_triggering import (
    ISignalTriggering,
)


class LinErrorResponse(ARObject):
    """AUTOSAR LinErrorResponse."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "response_error": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=ISignalTriggering,
        ),  # responseError
    }

    def __init__(self) -> None:
        """Initialize LinErrorResponse."""
        super().__init__()
        self.response_error: Optional[ISignalTriggering] = None


class LinErrorResponseBuilder:
    """Builder for LinErrorResponse."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: LinErrorResponse = LinErrorResponse()

    def build(self) -> LinErrorResponse:
        """Build and return LinErrorResponse object.

        Returns:
            LinErrorResponse instance
        """
        # TODO: Add validation
        return self._obj
