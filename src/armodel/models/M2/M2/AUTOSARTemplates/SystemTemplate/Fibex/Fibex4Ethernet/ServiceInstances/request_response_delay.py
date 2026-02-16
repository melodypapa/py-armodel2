"""RequestResponseDelay AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    TimeValue,
)


class RequestResponseDelay(ARObject):
    """AUTOSAR RequestResponseDelay."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "max_value": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # maxValue
        "min_value": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # minValue
    }

    def __init__(self) -> None:
        """Initialize RequestResponseDelay."""
        super().__init__()
        self.max_value: Optional[TimeValue] = None
        self.min_value: Optional[TimeValue] = None


class RequestResponseDelayBuilder:
    """Builder for RequestResponseDelay."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: RequestResponseDelay = RequestResponseDelay()

    def build(self) -> RequestResponseDelay:
        """Build and return RequestResponseDelay object.

        Returns:
            RequestResponseDelay instance
        """
        # TODO: Add validation
        return self._obj
